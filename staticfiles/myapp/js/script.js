// ============================================
// Run everything AFTER DOM is loaded
// ============================================
document.addEventListener("DOMContentLoaded", () => {

    // ============================================
    // IMAGE SLIDER
    // ============================================
    const track = document.querySelector(".slider-track");
    const slides = document.querySelectorAll(".slider-track img");
    let index = 0;

    if (track && slides.length > 0) {
        setInterval(() => {
            index++;

            if (index >= slides.length) {
                index = 0;
                track.style.transition = "none";
                track.style.transform = "translateX(0)";
                setTimeout(() => {
                    track.style.transition = "transform 0.8s ease-in-out";
                }, 50);
            } else {
                track.style.transform = `translateX(-${index * 100}%)`;
            }
        }, 5000);
    }

    // ============================================
    // TABS SWITCH LOGIC (SAME PAGE)
    // ============================================
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();

            const targetTab = btn.dataset.tab;

            // Remove active from all buttons
            tabButtons.forEach(b => b.classList.remove("active"));

            // Hide all tab contents
            tabContents.forEach(content => content.classList.remove("active"));

            // Activate clicked tab
            btn.classList.add("active");

            // Show corresponding section
            const targetSection = document.getElementById(targetTab);
            if (targetSection) {
                targetSection.classList.add("active");
            }
        });
    });

    // ============================================
    // CURRENCY INITIALIZATION
    // ============================================
    fetchRates().then(rates => {
        currentRates = rates;
        setDefaultFlag();
    });

});


// ============================================
// REAL-TIME CURRENCY CONVERTER
// ============================================
let currentRates = {};
let currentCurrency = "GBP";

async function fetchRates() {
    try {
        const response = await fetch("https://api.exchangerate-api.com/v4/latest/GBP");
        const data = await response.json();
        return data.rates;
    } catch (error) {
        console.error("Currency API error:", error);
        return {};
    }
}

function setDefaultFlag() {
    const flagImg = document.getElementById("selected-flag");
    if (flagImg) {
        flagImg.src = "https://flagcdn.com/24x18/gb.png";
        flagImg.style.display = "inline";
    }
}

function toggleDropdown() {
    const dropdown = document.getElementById("countryDropdown");
    if (dropdown) {
        dropdown.style.display =
            dropdown.style.display === "block" ? "none" : "block";
    }
}

function changeCurrency(currencyCode, flagCode) {
    const symbols = {
        GBP: "£",
        INR: "₹",
        USD: "$",
        AUD: "$",
        CAD: "C$",
        EUR: "€"
    };

    if (!currentRates[currencyCode]) {
        alert("Currency rates unavailable");
        return;
    }

    const rate = currentRates[currencyCode];
    const symbol = symbols[currencyCode];

    document.querySelectorAll("td[data-fee]").forEach(cell => {
        const base = Number(cell.dataset.fee);
        cell.textContent = symbol + Math.round(base * rate).toLocaleString();
    });

    const flagImg = document.getElementById("selected-flag");
    if (flagImg) {
        flagImg.src = `https://flagcdn.com/24x18/${flagCode}.png`;
        flagImg.style.display = "inline";
    }

    document.getElementById("countryDropdown").style.display = "none";
    currentCurrency = currencyCode;
}


// ============================================
// MOBILE MENU TOGGLE
// ============================================
function toggleMobileMenu() {
    const menu = document.getElementById("mobileMenu");
    if (menu) {
        menu.classList.toggle("show");
    }
}


// ============================================
// LOGIN / SIGNUP TOGGLE (IF USED)
// ============================================
function toggleForm() {
    document.getElementById("login-form")?.classList.toggle("hidden");
    document.getElementById("signup-form")?.classList.toggle("hidden");
}
