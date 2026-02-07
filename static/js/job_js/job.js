const root = document.documentElement;

/* THEME */
const themeBtn = document.getElementById("themeToggle");
const savedTheme = localStorage.getItem("theme");

if (savedTheme) root.setAttribute("data-theme", savedTheme);

themeBtn?.addEventListener("click", () => {
  const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
  root.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
});

/* ACCOUNT MENU */
const accountBtn = document.getElementById("accountToggle");
const accountMenu = document.getElementById("accountMenu");

accountBtn?.addEventListener("click", () => {
  accountMenu.classList.toggle("show");
});

document.addEventListener("click", e => {
  if (!accountBtn?.contains(e.target) && !accountMenu?.contains(e.target)) {
    accountMenu?.classList.remove("show");
  }
});
