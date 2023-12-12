const menuToggle = document.getElementById('menuToggle');
const menuIcon = document.getElementById('menuIcon');
const navLinks = document.getElementById('navLinks');

menuToggle.addEventListener('click', function () {
    navLinks.classList.toggle('hidden');
    menuIcon.classList.toggle('fa-bars');
    menuIcon.classList.toggle('fa-times');
});

anime.timeline({ loop: false }).add({
    targets: ".navbar-char-transition",
    opacity: [0, 1],
    easing: "easeInOutQuad",
    duration: 2000,
    delay: (el, i) => 150 * (i + 1),
});

anime
    .timeline({ loop: false })
    .add({
        targets: ".char-transition",
        opacity: [0, 1],
        easing: "easeInOutQuad",
        duration: 2000,
        delay: (el, i) => 150 * (i + 1),
    })
    .add({
        targets: "#basketball",
        translateX: 120, // Move to the right
        easing: "easeInOutQuad",
        duration: 800,
        rotate: 360, // Rotate 360 degrees
    })
    .add({
        targets: "#trophy",
        rotate: 15, // Tilt the trophy
        easing: "easeInOutQuad",
        duration: 500,
    });