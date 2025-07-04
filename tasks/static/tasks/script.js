document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.btn.delete').forEach(btn => {
    btn.addEventListener('click', (e) => {
      if (!confirm("Are you sure you want to delete this task?")) {
        e.preventDefault();
      }
    });
  });
});