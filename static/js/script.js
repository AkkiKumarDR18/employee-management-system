// Real-time Table Filter
function filterTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const rows = document.querySelectorAll("#employeeTable tbody tr");

    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? "" : "none";
    });
}


// Debounce for better performance
function debounce(func, delay = 300) {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

// Attach debounced filter
const searchInput = document.getElementById("searchInput");
if (searchInput) {
    searchInput.addEventListener("keyup", debounce(filterTable));
}


// Auto-dismiss Flash Messages
document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert");

    setTimeout(() => {
        alerts.forEach(alert => {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";
            setTimeout(() => alert.remove(), 500);
        });
    }, 3000);
});