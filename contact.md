---
layout: default
title: Contact
permalink: /contact/
---

<style>
    :root {
        --primary-color: #2C5F2D;
        --secondary-color: #1E2761;
        --accent-color: #735DA5;
        --gradient-primary: linear-gradient(135deg, #2C5F2D 0%, #31473A 100%);
        --gradient-secondary: linear-gradient(135deg, #1E2761 0%, #2C3E6E 100%);
        --gradient-accent: linear-gradient(135deg, #735DA5 0%, #8B7CB5 100%);
        --text-dark: #2D3748;
        --text-light: #4A5568;
        --bg-light: #F7FAFC;
        --border-color: #E2E8F0;
    }

    .contact-container {
        margin: 0 auto;
        padding: 0.5rem 2rem;
        max-width: 1200px;
        box-sizing: border-box;
    }

    .contact-header {
        text-align: center;
        margin-top: 0.1rem;
        margin-bottom: 0.8rem;
        padding: 0.8rem;
        background: transparent;
        border-radius: 16px;
        color: inherit;
        box-shadow: none;
    }

    .contact-title {
        font-size: 2rem;
        margin-top: 0.1rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
        color: var(--heading-color);
    }

    .contact-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
        color: var(--text-light);
    }

    .contact-section {
        margin: 2rem 0;
    }

    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .contact-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .contact-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--gradient-accent);
    }

    .contact-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
        border-color: rgba(115, 93, 165, 0.2);
    }

    .contact-method {
        font-size: 1.2rem;
        color: var(--secondary-color);
        margin-bottom: 1rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .contact-icon {
        width: 24px;
        height: 24px;
        color: var(--accent-color);
    }

    .contact-details {
        font-size: 1rem;
        color: var(--text-light);
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .map-iframe {
        width: 100%;
        height: 280px;
        border: 0;
        border-radius: 12px;
    }

    .contact-link {
        color: var(--accent-color);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }

    .contact-link:hover {
        color: var(--primary-color);
        text-decoration: underline;
    }

    .contact-form {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid var(--border-color);
        margin-top: 2rem;
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    .form-label {
        display: block;
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-dark);
        margin-bottom: 0.5rem;
    }

    .form-input,
    .form-textarea {
        width: 100%;
        padding: 0.75rem 1rem;
        border: 2px solid var(--border-color);
        border-radius: 8px;
        font-size: 1rem;
        font-family: inherit;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    .form-input:focus,
    .form-textarea:focus {
        outline: none;
        border-color: var(--accent-color);
        box-shadow: 0 0 0 3px rgba(115, 93, 165, 0.1);
    }

    .form-textarea {
        resize: vertical;
        min-height: 120px;
    }

    .submit-btn {
        background: var(--gradient-primary);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 9999px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(44, 95, 45, 0.3);
    }

    .submit-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(44, 95, 45, 0.4);
    }

    .lab-location {
        background: var(--bg-light);
        padding: 2rem;
        border-radius: 16px;
        border-left: 4px solid var(--primary-color);
        margin-top: 2rem;
    }

    .lab-location h3 {
        color: var(--primary-color);
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }

    .lab-location p {
        color: var(--text-dark);
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }

    .back-link {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: var(--primary-color);
        text-decoration: none;
        font-weight: 500;
        margin-top: 2rem;
        padding: 0.8rem 1.5rem;
        background: white;
        border: 2px solid var(--primary-color);
        border-radius: 9999px;
        transition: all 0.3s ease;
    }

    .back-link:hover {
        background: var(--gradient-primary);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(44, 95, 45, 0.3);
    }

    /* Animation for scroll reveal */
    .fade-in {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.6s ease;
    }

    .fade-in.visible {
        opacity: 1;
        transform: translateY(0);
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .contact-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .contact-title {
            font-size: 2rem;
        }
        
        .contact-header {
            padding: 1.5rem;
        }
        
        .contact-card {
            padding: 1.5rem;
        }
        
        .contact-form {
            padding: 1.5rem;
        }
    }

    @media (max-width: 480px) {
        .contact-container {
            padding: 1rem 0.75rem;
        }
        
        .contact-header {
            padding: 1rem;
        }
        
        .contact-title {
            font-size: 1.8rem;
        }
    }
</style>

<div class="contact-container">
    <div class="contact-header fade-in">
        <h1 class="contact-title">Contact Us</h1>
        <p class="contact-subtitle">We welcome inquiries about our research, collaborations, and opportunities. Please feel free to reach out through any of the channels below.</p>
    </div>
    <div class="contact-section">
        <div class="contact-grid">
            
            <div class="contact-card fade-in">
                <h3 class="contact-method">
                    <svg class="contact-icon" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
                        <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
                    </svg>
                    Email
                </h3>
                <div class="contact-details">
                    <p>For research inquiries and collaborations:</p>
                    <a href="mailto:fengyuanqing2010@gmail.com" class="contact-link">fengyuanqing2010@gmail.com</a>
                </div>
            </div>
            
            <div class="contact-card fade-in">
                <h3 class="contact-method">
                    <svg class="contact-icon" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path>
                    </svg>
                    Address
                </h3>
                <div class="contact-details">
                    <p>China Pharmaceutical University<br>
                    School of Basic and Clinical Medicine</p>
                </div>
            </div>

            <div class="contact-card fade-in">
                <h3 class="contact-method">
                    <svg class="contact-icon" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path>
                    </svg>
                    Map
                </h3>
                <div class="contact-details">
                    <iframe class="map-iframe" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=%E4%B8%AD%E5%9B%BD%E8%8D%AF%E7%A7%91%E5%A4%A7%E5%AD%A6%E6%B1%9F%E5%AE%81%E6%A0%A1%E5%8C%BA&output=embed"></iframe>
                </div>
            </div>
            
        </div>
        
    </div>
    
    <div style="text-align: center; margin-top: 3rem;">
        <a href="/" class="back-link">
            <i class="fas fa-home"></i>
            Back to Homepage
        </a>
    </div>
</div>

<script>
    // Intersection Observer for fade-in animations
    document.addEventListener('DOMContentLoaded', function() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, index * 100);
                }
            });
        }, { threshold: 0.1 });
        
        const fadeElements = document.querySelectorAll('.fade-in');
        fadeElements.forEach(el => observer.observe(el));
    });
</script>
