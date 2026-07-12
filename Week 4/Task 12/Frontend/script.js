/**
 * Shared JavaScript for Kyphosis Prediction App
 * Handles navigation highlighting, API calls, and common functionality
 */

// Configuration
const API_BASE_URL = 'http://localhost:8000';

/**
 * Initialize the application
 */
function init() {
    // Highlight current page in navigation
    highlightCurrentPage();
    
    // Setup mobile navigation toggle
    setupMobileNav();
    
    // Add keyboard navigation
    addKeyboardNavigation();
    
    // Initialize animated background
    initAnimatedBackground();
    
    // Initialize custom cursor
    initCustomCursor();
    
    console.log('Kyphosis Prediction App initialized');
}

/**
 * Initialize animated starfield background
 */
function initAnimatedBackground() {
    const starsContainer = document.createElement('div');
    starsContainer.className = 'stars-container';
    document.body.appendChild(starsContainer);
    
    // Create twinkling stars
    for (let i = 0; i < 100; i++) {
        createStar(starsContainer);
    }
    
    // Create occasional shooting stars
    setInterval(() => {
        if (Math.random() < 0.1) { // 10% chance every interval
            createShootingStar(starsContainer);
        }
    }, 3000);
}

/**
 * Create a twinkling star
 */
function createStar(container) {
    const star = document.createElement('div');
    star.className = 'star';
    
    // Random position
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    
    // Random size (1-3px)
    const size = Math.random() * 2 + 1;
    star.style.width = size + 'px';
    star.style.height = size + 'px';
    
    // Random animation duration (2-4 seconds)
    star.style.animationDuration = (Math.random() * 2 + 2) + 's';
    
    // Random delay
    star.style.animationDelay = Math.random() * 3 + 's';
    
    container.appendChild(star);
}

/**
 * Create a shooting star
 */
function createShootingStar(container) {
    const shootingStar = document.createElement('div');
    shootingStar.className = 'shooting-star';
    
    // Random starting position (off-screen left, random height)
    shootingStar.style.left = '-100px';
    shootingStar.style.top = Math.random() * 50 + '%';
    
    // Random width (50-200px)
    shootingStar.style.width = (Math.random() * 150 + 50) + 'px';
    
    // Random animation duration (3-6 seconds)
    shootingStar.style.animationDuration = (Math.random() * 3 + 3) + 's';
    
    container.appendChild(shootingStar);
    
    // Remove after animation
    setTimeout(() => {
        if (shootingStar.parentNode) {
            shootingStar.parentNode.removeChild(shootingStar);
        }
    }, 8000);
}

/**
 * Initialize custom cursor glow effect
 */
function initCustomCursor() {
    // Don't show custom cursor on touch devices
    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
        document.body.style.cursor = 'default';
        return;
    }
    
    const cursorGlow = document.createElement('div');
    cursorGlow.className = 'cursor-glow';
    document.body.appendChild(cursorGlow);
    
    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;
    
    // Track mouse movement
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });
    
    // Smooth cursor following animation
    function animateCursor() {
        const dx = mouseX - cursorX;
        const dy = mouseY - cursorY;
        
        cursorX += dx * 0.1;
        cursorY += dy * 0.1;
        
        cursorGlow.style.left = (cursorX - 20) + 'px';
        cursorGlow.style.top = (cursorY - 20) + 'px';
        
        requestAnimationFrame(animateCursor);
    }
    
    animateCursor();
    
    // Hide cursor when leaving window
    document.addEventListener('mouseleave', () => {
        cursorGlow.style.opacity = '0';
    });
    
    document.addEventListener('mouseenter', () => {
        cursorGlow.style.opacity = '1';
    });
    
    // Enhance cursor on hover over interactive elements
    const interactiveElements = 'a, button, input, .nav-toggle, .sample-case, .tech-card';
    
    document.addEventListener('mouseover', (e) => {
        if (e.target.matches(interactiveElements)) {
            cursorGlow.style.transform = 'scale(1.5)';
            cursorGlow.style.background = `radial-gradient(
                circle,
                rgba(135, 206, 235, 1) 0%,
                rgba(135, 206, 235, 0.6) 30%,
                rgba(135, 206, 235, 0.2) 60%,
                transparent 100%
            )`;
        }
    });
    
    document.addEventListener('mouseout', (e) => {
        if (e.target.matches(interactiveElements)) {
            cursorGlow.style.transform = 'scale(1)';
            cursorGlow.style.background = `radial-gradient(
                circle,
                rgba(135, 206, 235, 0.8) 0%,
                rgba(135, 206, 235, 0.4) 30%,
                rgba(135, 206, 235, 0.1) 60%,
                transparent 100%
            )`;
        }
    });
}

/**
 * Highlight the current page in navigation
 */
function highlightCurrentPage() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || 
           (currentPage === '' && href === 'index.html') ||
           (currentPage === 'index.html' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

/**
 * Setup mobile navigation toggle
 */
function setupMobileNav() {
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
        
        // Close mobile nav when clicking a link
        navLinks.addEventListener('click', (e) => {
            if (e.target.tagName === 'A') {
                navLinks.classList.remove('active');
            }
        });
    }
}

/**
 * Add keyboard navigation support
 */
function addKeyboardNavigation() {
    document.addEventListener('keydown', (event) => {
        // Escape key closes mobile nav
        if (event.key === 'Escape') {
            const navLinks = document.querySelector('.nav-links');
            if (navLinks) {
                navLinks.classList.remove('active');
            }
        }
    });
}

/**
 * Fetch model metrics from API
 */
async function fetchModelMetrics() {
    try {
        const response = await fetch(`${API_BASE_URL}/metrics`);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch metrics:', error);
        throw new Error('Unable to load model metrics. Please ensure the backend server is running.');
    }
}

/**
 * Make prediction API call
 */
async function makePrediction(formData) {
    console.log('Making prediction with data:', formData);
    
    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    });
    
    console.log('Response status:', response.status);
    
    if (!response.ok) {
        let errorMsg = 'Network error occurred';
        
        try {
            const errorData = await response.json();
            errorMsg = errorData.detail || `Server error: ${response.status}`;
        } catch (e) {
            if (response.status === 0 || !response.status) {
                errorMsg = 'Cannot connect to server. Please make sure the backend is running on http://localhost:8000';
            } else {
                errorMsg = `Server error: ${response.status} ${response.statusText}`;
            }
        }
        
        throw new Error(errorMsg);
    }
    
    const result = await response.json();
    console.log('Prediction result:', result);
    return result;
}

/**
 * Check API health
 */
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (response.ok) {
            console.log('✅ Backend API is running');
            return true;
        } else {
            console.warn('⚠️ Backend API returned non-OK status');
            return false;
        }
    } catch (error) {
        console.warn('⚠️ Cannot connect to backend API:', error.message);
        return false;
    }
}

/**
 * Display error message in a standardized way
 */
function displayError(message, containerId = 'error-container') {
    const errorContainer = document.getElementById(containerId);
    if (errorContainer) {
        errorContainer.innerHTML = `
            <div class="card" style="border-color: #ef4444; background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%);">
                <h3 style="color: #fca5a5;">Error</h3>
                <p style="color: #fecaca;">${message}</p>
            </div>
        `;
        errorContainer.style.display = 'block';
        errorContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

/**
 * Hide error message
 */
function hideError(containerId = 'error-container') {
    const errorContainer = document.getElementById(containerId);
    if (errorContainer) {
        errorContainer.style.display = 'none';
    }
}

/**
 * Show loading state for a button
 */
function setButtonLoading(button, loading = true) {
    if (loading) {
        // Store original text if not already stored
        if (!button.dataset.originalText) {
            button.dataset.originalText = button.textContent;
        }
        button.disabled = true;
        button.innerHTML = '<span class="loading-spinner"></span>Processing...';
    } else {
        button.disabled = false;
        button.innerHTML = button.dataset.originalText || 'Predict Kyphosis Risk';
    }
}

/**
 * Validate form input
 */
function validateInput(value, min, max, fieldName) {
    const num = parseInt(value);
    
    if (isNaN(num)) {
        return `${fieldName} must be a valid number`;
    }
    
    if (num < min || num > max) {
        return `${fieldName} must be between ${min} and ${max}`;
    }
    
    return null;
}

/**
 * Format percentage for display
 */
function formatPercentage(decimal) {
    return Math.round(decimal * 100);
}

/**
 * Animate confidence bar
 */
function animateConfidenceBar(confidence) {
    const bar = document.querySelector('.confidence-fill');
    const text = document.querySelector('.confidence-text');
    
    if (bar && text) {
        // Start at 0 width
        bar.style.width = '0%';
        
        // Animate to final width
        setTimeout(() => {
            const percentage = formatPercentage(confidence);
            bar.style.width = `${percentage}%`;
            text.textContent = `Confidence: ${percentage}%`;
        }, 100);
    }
}

/**
 * Smooth scroll to element
 */
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

/**
 * Initialize page-specific functionality
 */
function initPageSpecific() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    
    switch (currentPage) {
        case 'predict.html':
            if (typeof initPredictPage === 'function') {
                initPredictPage();
            }
            break;
        case 'about.html':
            if (typeof initAboutPage === 'function') {
                initAboutPage();
            }
            break;
        case 'index.html':
        case '':
            if (typeof initHomePage === 'function') {
                initHomePage();
            }
            break;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    init();
    initPageSpecific();
    
    // Check API health on startup
    checkAPIHealth();
});

// Handle network status
window.addEventListener('online', function() {
    console.log('✅ Network connection restored');
    hideError('network-error');
});

window.addEventListener('offline', function() {
    console.warn('⚠️ Network connection lost');
    displayError('Network connection lost. Please check your internet connection.', 'network-error');
});