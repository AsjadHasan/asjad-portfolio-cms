/**
 * Main client interactions: accessible mobile menu, theme preference,
 * scroll reveals, header shadow, and project category filtering.
 */
(() => {
  "use strict";

  const root = document.documentElement;
  const themeButton = document.querySelector("#theme-toggle");
  const themeIcon = document.querySelector("#theme-icon");
  const menuButton = document.querySelector("#menu-toggle");
  const menu = document.querySelector("#site-nav");
  const header = document.querySelector("#site-header");

  /** Apply the requested color theme and optionally persist it. */
  function setTheme(theme, persist = false) {
    const normalized = theme === "light" ? "light" : "dark";
    root.dataset.theme = normalized;
    if (themeButton) {
      themeButton.setAttribute("aria-label", `Switch to ${normalized === "dark" ? "light" : "dark"} mode`);
    }
    if (themeIcon) themeIcon.textContent = normalized === "dark" ? "☀" : "☾";
    if (persist) {
      try { localStorage.setItem("asjad-theme", normalized); } catch (_) { /* Storage may be blocked. */ }
    }
  }

  let savedTheme = "dark";
  try { savedTheme = localStorage.getItem("asjad-theme") || "dark"; } catch (_) { /* No storage. */ }
  setTheme(savedTheme);
  themeButton?.addEventListener("click", () => {
    setTheme(root.dataset.theme === "dark" ? "light" : "dark", true);
  });

  /** Open or close the mobile navigation, preserving ARIA state. */
  function toggleMenu(open) {
    if (!menu || !menuButton) return;
    menu.classList.toggle("is-open", open);
    menuButton.setAttribute("aria-expanded", String(open));
    menuButton.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }
  menuButton?.addEventListener("click", () => toggleMenu(!menu.classList.contains("is-open")));
  menu?.querySelectorAll("a").forEach(link => link.addEventListener("click", () => toggleMenu(false)));
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") toggleMenu(false);
  });
  document.addEventListener("click", event => {
    if (menu?.classList.contains("is-open") && !menu.contains(event.target) && !menuButton?.contains(event.target)) toggleMenu(false);
  });

  /** Show a thin separator after the user scrolls. */
  function updateHeader() { header?.classList.toggle("is-scrolled", window.scrollY > 18); }
  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });

  /** Animate visible sections only when motion is allowed. */
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduceMotion && "IntersectionObserver" in window) {
    root.classList.add("js-enabled");
    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          currentObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -25px 0px" });
    document.querySelectorAll("[data-reveal]").forEach(element => observer.observe(element));
  }

  /** Instantly filter project cards without requesting another page. */
  const filterButtons = [...document.querySelectorAll("[data-filter]")];
  const projectCards = [...document.querySelectorAll("[data-category]")];
  const emptyFilterMessage = document.querySelector("#filter-empty");
  filterButtons.forEach(button => {
    button.addEventListener("click", () => {
      const category = button.dataset.filter;
      let visibleCount = 0;
      filterButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", String(active));
      });
      projectCards.forEach(card => {
        const visible = category === "all" || card.dataset.category === category;
        card.hidden = !visible;
        if (visible) visibleCount++;
      });
      if (emptyFilterMessage) emptyFilterMessage.hidden = visibleCount !== 0;
    });
  });
})();
