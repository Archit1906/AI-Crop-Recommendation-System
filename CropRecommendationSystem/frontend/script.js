const API_URL = "http://127.0.0.1:8000";

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    const formSection = document.getElementById('formSection');
    const resultSection = document.getElementById('resultSection');
    const submitBtn = document.getElementById('submitBtn');
    const spinner = document.getElementById('spinner');
    const btnText = submitBtn.querySelector('span');
    const backBtn = document.getElementById('backBtn');
    const errorAlert = document.getElementById('errorAlert');
    const errorText = document.getElementById('errorText');
    const closeError = document.getElementById('closeError');

    // Emoji mapping for common crops
    const cropEmojis = {
        'rice': '🌾', 'maize': '🌽', 'chickpea': '🧆', 'kidneybeans': '🫘',
        'pigeonpeas': '🌱', 'mothbeans': '🌿', 'mungbean': '🌱', 'blackgram': '🪴',
        'lentil': '🍲', 'pomegranate': '🍎', 'banana': '🍌', 'mango': '🥭',
        'grapes': '🍇', 'watermelon': '🍉', 'muskmelon': '🍈', 'apple': '🍏',
        'orange': '🍊', 'papaya': '🥑', 'coconut': '🥥', 'cotton': '☁️',
        'jute': '🧶', 'coffee': '☕'
    };

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Hide previous errors
        errorAlert.classList.add('hidden');

        // Prepare Data
        const formData = new FormData(form);
        const submitData = {};

        // Process inputs
        for (let [key, value] of formData.entries()) {
            if (value !== '') {
                submitData[key] = isNaN(value) ? value : parseFloat(value);
            }
        }

        // UX: Loading state
        submitBtn.disabled = true;
        btnText.textContent = "Analyzing...";
        spinner.style.display = "block";

        try {
            const response = await fetch(`${API_URL}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(submitData)
            });

            const data = await response.json();

            if (!response.ok) {
                // If API returns 400 or 500, throw error detail
                throw new Error(data.detail || "Failed to get recommendation");
            }

            displayResult(data);

        } catch (error) {
            showError(error.message);
        } finally {
            // Revert UX
            submitBtn.disabled = false;
            btnText.textContent = "Get Recommendation";
            spinner.style.display = "none";
        }
    });

    function displayResult(data) {
        // Populate Result Data
        document.getElementById('predictedCrop').textContent = data.crop;
        document.getElementById('predictionConfidence').textContent = data.confidence;

        const emoji = cropEmojis[data.crop.toLowerCase()] || '🌾';
        document.getElementById('cropNameLetter').textContent = emoji;

        document.getElementById('tipIrrigation').textContent = data.tips.irrigation;
        document.getElementById('tipSoil').textContent = data.tips.soil;
        document.getElementById('tipClimate').textContent = data.tips.climate;

        // Animate Panel Switch
        formSection.style.opacity = "0";
        setTimeout(() => {
            formSection.classList.add('hidden');
            resultSection.classList.remove('hidden');
            // trigger reflow
            void resultSection.offsetWidth;
            resultSection.style.opacity = "1";
        }, 300);
    }

    backBtn.addEventListener('click', () => {
        resultSection.style.opacity = "0";
        setTimeout(() => {
            resultSection.classList.add('hidden');
            formSection.classList.remove('hidden');
            void formSection.offsetWidth;
            formSection.style.opacity = "1";
        }, 300);
    });

    closeError.addEventListener('click', () => {
        errorAlert.classList.add('hidden');
    });

    function showError(msg) {
        errorText.textContent = msg;
        errorAlert.classList.remove('hidden');
        // Auto hide after 5 seconds
        setTimeout(() => {
            errorAlert.classList.add('hidden');
        }, 5000);
    }
});
