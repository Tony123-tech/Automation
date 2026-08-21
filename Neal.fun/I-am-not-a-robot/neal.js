function runCaptchaBot() {
    let level1Box = document.querySelector('.checkmark-spinner-container') || document.querySelector('.checkbox');
    if (level1Box) {
        level1Box.click();
        setTimeout(runCaptchaBot, 5000);
        return;
    }

    let gridItems = document.querySelectorAll('.grid-item');
    if (gridItems.length > 0) {
        let targets = [2, 3, 6, 7]; 
        targets.forEach(index => {
            if (gridItems[index]) gridItems[index].click();
        });

        setTimeout(() => {
            document.querySelector('#captcha-verify-button')?.click();
            setTimeout(runCaptchaBot, 5000);
        }, 5000);
        return;
    }

runCaptchaBot()
