(function () {
  "use strict";

  const form = document.getElementById("teamForm");
  if (!form) return;

  const field = (id) => document.getElementById(id);
  const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
  const saveButton = field("saveButton");

  function slugify(value) {
    return value.toLowerCase().trim().replace(/[^a-z0-9\s-]/g, "").replace(/[\s_-]+/g, "-").replace(/^-+|-+$/g, "");
  }

  async function responseJson(response) {
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !data.success) throw new Error(data.message || "Request failed.");
    return data;
  }

  async function copyText(value) {
    if (!value) return;
    try {
      await navigator.clipboard.writeText(value);
      alert("Profile URL copied.");
    } catch (_) {
      field("public_url").select();
      document.execCommand("copy");
      alert("Profile URL copied.");
    }
  }

  field("name").addEventListener("input", function () {
    if (!field("team_id").value) {
      field("public_url").value = window.location.origin + "/" + (slugify(this.value) || "member-name") + "/";
    }
  });

  field("image").addEventListener("change", function () {
    const file = this.files[0];
    if (file) field("imagePreview").innerHTML = '<img src="' + URL.createObjectURL(file) + '" alt="Preview" width="110" height="110" class="rounded-circle border" style="object-fit:cover">';
  });

  field("copyUrlButton").addEventListener("click", () => copyText(field("public_url").value));

  document.addEventListener("click", async function (event) {
    const copyButton = event.target.closest(".copy-team-url");
    if (copyButton) return copyText(copyButton.dataset.url);

    const editButton = event.target.closest(".edit-team");
    if (editButton) {
      try {
        const data = await fetch("/dashboard/team/get/" + editButton.dataset.id + "/", { headers: { Accept: "application/json" } }).then(responseJson);
        const member = data.team;
        field("team_id").value = member.id;
        ["name", "designation", "email", "phone", "linkedin", "bio"].forEach((key) => { field(key).value = member[key] || ""; });
        field("status").value = member.status ? "1" : "0";
        field("public_url").value = member.public_url;
        field("imagePreview").innerHTML = member.image_url ? '<img src="' + member.image_url + '" alt="Current image" width="110" height="110" class="rounded-circle border" style="object-fit:cover">' : "";
        field("formTitle").textContent = "Edit Team Member";
        saveButton.textContent = "Update Team Member";
        window.scrollTo({ top: 0, behavior: "smooth" });
      } catch (error) {
        alert(error.message);
      }
      return;
    }

    const deleteButton = event.target.closest(".delete-team");
    if (deleteButton) {
      if (!confirm('Delete "' + deleteButton.dataset.name + '"? This cannot be undone.')) return;
      try {
        await fetch("/dashboard/team/delete/" + deleteButton.dataset.id + "/", {
          method: "POST", headers: { "X-CSRFToken": csrfToken, Accept: "application/json" }
        }).then(responseJson);
        window.location.reload();
      } catch (error) {
        alert(error.message);
      }
    }
  });

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    const memberId = field("team_id").value;
    saveButton.disabled = true;
    try {
      const data = await fetch(memberId ? "/dashboard/team/edit/" + memberId + "/" : "/dashboard/team/add/", {
        method: "POST", body: new FormData(form), headers: { "X-CSRFToken": csrfToken, Accept: "application/json" }
      }).then(responseJson);
      alert(data.message);
      window.location.reload();
    } catch (error) {
      alert(error.message);
      saveButton.disabled = false;
    }
  });
})();
