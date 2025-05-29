document.addEventListener("DOMContentLoaded", function() {
    const inquiryForm = document.getElementById("inquiryForm");
    if (inquiryForm) {
        inquiryForm.addEventListener("submit", function(e) {
            e.preventDefault();
            fetch("/add-inquiry/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: JSON.stringify({
                    name: document.getElementById("name").value,
                    email: document.getElementById("email").value,
                    carModel: document.getElementById("carModel").value,
                    message: document.getElementById("message").value
                })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || "تم إرسال الاستفسار!");
                inquiryForm.reset();
            })
            .catch(() => alert("حدث خطأ أثناء الإرسال!"));
        });
    }

    // Theme toggle
    const themeToggle = document.getElementById("themeToggle");
    if (themeToggle) {
        themeToggle.addEventListener("click", function() {
            document.body.classList.toggle("dark-mode");
            if(document.body.classList.contains("dark-mode")) {
                localStorage.setItem("theme", "dark");
                themeToggle.textContent = "☀️ الوضع النهاري";
            } else {
                localStorage.setItem("theme", "light");
                themeToggle.textContent = "🌙 الوضع الليلي";
            }
        });

        if(localStorage.getItem("theme") === "dark") {
            document.body.classList.add("dark-mode");
            themeToggle.textContent = "☀️ الوضع النهاري";
        }
    }

    // البحث عن سيارة
    const searchBar = document.getElementById("searchBar");
    if (searchBar) {
        searchBar.addEventListener("input", function() {
            const query = this.value.trim().toLowerCase();
            document.querySelectorAll(".car-card").forEach(card => {
                const name = card.querySelector("h2")?.textContent.toLowerCase() || "";
                const desc = card.querySelector("p")?.textContent.toLowerCase() || "";
                if (name.includes(query) || desc.includes(query)) {
                    card.style.display = "";
                } else {
                    card.style.display = "none";
                }
            });
        });
    }
});

// دالة لجلب CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}