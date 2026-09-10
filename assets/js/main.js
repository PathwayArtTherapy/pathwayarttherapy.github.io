/* Pathway Art Therapy — small site script: mobile menu + contact form */

// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("site-nav");
if (toggle && nav) {
  const setOpen = (open) => {
    nav.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", String(open));
    document.body.classList.toggle("menu-open", open);
  };
  toggle.addEventListener("click", () => setOpen(!nav.classList.contains("open")));
  nav.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
}

// Contact forms, sent through Web3Forms (https://web3forms.com)
document.querySelectorAll("form[data-web3forms]").forEach((form) => {
  const status = form.querySelector(".form-status");
  const button = form.querySelector('button[type="submit"]');

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (form.querySelector('[name="botcheck"]')?.checked) return; // spam bot

    const label = button.textContent;
    button.disabled = true;
    button.textContent = "Sending…";
    status.className = "form-status";
    status.textContent = "";

    try {
      const res = await fetch(form.action, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(Object.fromEntries(new FormData(form))),
      });
      const data = await res.json();
      if (!res.ok || !data.success) throw new Error(data.message || "Send failed");
      form.reset();
      status.classList.add("ok");
      status.textContent = "Thank you! Your message is on its way, and I'll be in touch soon.";
    } catch (err) {
      status.classList.add("err");
      status.innerHTML = 'Sorry, that didn’t send. Please try again, or email me at <a href="mailto:loulou@pathwayarttherapy.com">loulou@pathwayarttherapy.com</a>.';
    } finally {
      button.disabled = false;
      button.textContent = label;
    }
  });
});
