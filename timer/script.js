const countdownDate = new Date("2024-12-31T00:00:00").getTime();

const updateCountdown = () => {
    const now = new Date().getTime();
    const distance = countdownDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("days").textContent = String(days).padStart(2, '0');
    document.getElementById("hours").textContent = String(hours).padStart(2, '0');
    document.getElementById("minutes").textContent = String(minutes).padStart(2, '0');
    document.getElementById("seconds").textContent = String(seconds).padStart(2, '0');

    if (distance < 0) {
        clearInterval(timer);
        document.querySelector('.container').innerHTML = "LAUNCHED!";
    }
};

const timer = setInterval(updateCountdown, 1000);

    /* Add event listener for mobile devices */
    window.addEventListener('resize', function() {
        if (window.innerWidth <= 768) {
            document.querySelector('.container').style.display = 'flex';
            document.querySelector('.countdown').style.display = 'none';
        } else {
            document.querySelector('.container').style.display = 'block';
            document.querySelector('.countdown').style.display = 'flex';
        }
    });