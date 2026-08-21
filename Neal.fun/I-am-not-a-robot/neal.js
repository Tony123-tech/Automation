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

    let inputField = document.querySelector('.captcha-input-text');
    let submitBtn = document.querySelector('.captcha-button-valid');
    if (inputField && submitBtn) {
        let appElement = document.querySelector('#__nuxt') || document.querySelector('[data-v-app]') || document.body;
        let vueInstance = appElement.__vue_app__?._container?._vnode?.component?.ctx || appElement.__vue__;

        if (vueInstance) {
            let correctAnswer = vueInstance.captchaText || vueInstance.$data?.captchaText || 
                                vueInstance.text || vueInstance.$data?.text || 
                                vueInstance.answer || vueInstance.$data?.answer;

            if (correctAnswer) {
                inputField.value = correctAnswer;
                inputField.dispatchEvent(new Event('input', { bubbles: true }));

                setTimeout(() => {
                    submitBtn.click();
                    setTimeout(runCaptchaBot, 5000);
                }, 5000);
            }
        }
    }
}

runCaptchaBot();
