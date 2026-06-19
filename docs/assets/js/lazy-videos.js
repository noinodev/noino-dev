document.addEventListener("DOMContentLoaded", () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const video = entry.target;

      video.querySelectorAll("source[data-src]").forEach(source => {
        source.src = source.dataset.src;
      });

      video.load();

      if (video.hasAttribute("autoplay")) {
        video.play().catch(() => {});
      }

      observer.unobserve(video);
    });
  }, {
    rootMargin: "200px"
  });

  document.querySelectorAll("video.lazy-video").forEach(video => {
    observer.observe(video);
  });
});