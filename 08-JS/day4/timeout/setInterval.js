function showBanner() {
  const banner = document.getElementById('sales-banner');
  banner.style.display = 'block';

  let countdown = 10; // countdown from 10

  function updateBannerText() {
    banner.textContent = `The sales end in ${countdown} sec!`;
    countdown--;

    if (countdown < 0) {
      clearInterval(countdownInterval);
    }
  }

  const countdownInterval = setInterval(updateBannerText, 1000);
}

setTimeout(showBanner, 5000);
