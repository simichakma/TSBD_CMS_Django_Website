(function () {
  "use strict";
  const root = document.getElementById("memberDetail");
  if (!root) return;

  function setContact(rowId, linkId, value, prefix) {
    if (!value) return;
    const row = document.getElementById(rowId);
    const link = document.getElementById(linkId);
    link.textContent = value;
    row.href = prefix + value;
    row.hidden = false;
  }

  fetch(root.dataset.apiUrl, { headers: { Accept: "application/json" } })
    .then(function (response) { if (!response.ok) throw new Error("Profile unavailable"); return response.json(); })
    .then(function (data) {
      const member = data.member;
      document.title = member.name + " | Team Solutions Bangladesh";
      document.getElementById("memberName").textContent = member.name;
      document.getElementById("memberDesignation").textContent = member.designation || "";
      const image = document.getElementById("memberImage");
      if (member.image_url) {
        const photo = document.createElement("img");
        photo.src = member.image_url; photo.alt = member.name; image.appendChild(photo);
      } else {
        const avatar = document.createElement("div");
        avatar.className = "team-avatar team-avatar-large";
        avatar.setAttribute("aria-label", "Default user icon");
        avatar.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0 2c-5.33 0-8 2.67-8 5v3h16v-3c0-2.33-2.67-5-8-5Z"/></svg>';
        image.appendChild(avatar);
      }
      setContact("memberEmailRow", "memberEmail", member.email, "mailto:");
      setContact("memberPhoneRow", "memberPhone", member.phone, "tel:");
      if (member.linkedin) {
        const linkedinRow = document.getElementById("memberLinkedinRow");
        linkedinRow.href = member.linkedin;
        linkedinRow.hidden = false;
      }
      document.getElementById("memberBio").textContent = member.bio || "No biography has been added yet.";
    })
    .catch(function () {
      document.getElementById("memberName").textContent = "Profile unavailable";
      document.getElementById("memberDesignation").textContent = "Please return to the team page and try again.";
    });
})();
