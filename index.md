---
layout: default
title: Home
---

<style>
    .hero-section {
        text-align: center;
        padding: 2.8rem 1.5rem 3.5rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 24px;
        max-width: 1200px;
        margin: 1.25rem auto 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 24px 70px rgba(23, 37, 84, 0.1);
        min-height: clamp(420px, 63vh, 644px);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        gap: 1.4rem;
        box-sizing: border-box;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: var(--gradient-secondary);
        border-radius: 3px 3px 0 0;
        z-index: 2;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        inset: 0;
        background-image: url('/assets/images/background2.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: 50% 45%;
        opacity: 0.5;
        filter: brightness(0.9);
        z-index: 0;
        transform: none;
    }
    
    .hero-section > * {
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        font-size: clamp(3rem, 4vw, 4.25rem);
        font-weight: 700;
        margin-bottom: 1.05rem;
        background: var(--gradient-secondary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        line-height: 1.1;
        margin-top: -0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: var(--text-dark);
        margin-bottom: 2.1rem;
        font-weight: 600;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }
    
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.875rem 2rem;
        border: none;
        border-radius: 9999px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        font-size: 1rem;
        line-height: 1;
        position: relative;
        overflow: hidden;
        min-width: 140px;
    }
    
    .btn-primary {
        background: var(--gradient-primary);
        color: white;
        box-shadow: var(--shadow-light);
    }
    
    .btn-primary:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--shadow-medium);
        color: white;
    }
    
    .hero-ticker {
        width: min(720px, 90vw);
        background: rgba(255, 255, 255, 0.8);
        border-radius: 24px;
        padding: 0.72rem 1.3rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        border: 1px solid rgba(134, 151, 214, 0.4);
        box-shadow: 0 20px 45px rgba(30, 41, 59, 0.15);
        backdrop-filter: blur(14px);
        margin: 1.5rem auto 0;
        min-height: 51px;
    }
    
    .ticker-label {
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #2f3f7f;
    }
    
    .ticker-track {
        flex: 1;
        position: relative;
        overflow: hidden;
        height: 2.56rem;
        display: flex;
        align-items: center;
    }
    
    .ticker-track::before,
    .ticker-track::after {
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        height: 18px;
        pointer-events: none;
        z-index: 2;
    }
    
    .ticker-track::before {
        top: 0;
        background: linear-gradient(180deg, rgba(248, 250, 255, 0.85), transparent);
    }
    
    .ticker-track::after {
        bottom: 0;
        background: linear-gradient(0deg, rgba(248, 250, 255, 0.85), transparent);
    }
    
    .ticker-inner {
        display: flex;
        flex-direction: column;
        gap: 0;
        animation: tickerScrollY 20s linear infinite;
        animation-play-state: running;
    }

    .hero-ticker:hover .ticker-inner {
        animation-play-state: paused;
    }
    
    .ticker-item {
        white-space: nowrap;
        font-weight: 600;
        color: #1f2a44;
        font-size: 0.98rem;
        display: flex;
        align-items: center;
        gap: 0.65rem;
        min-height: 1.92rem;
        padding: 0.2rem 0;
        text-decoration: none;
    }
    
    .ticker-date {
        font-size: 0.85rem;
        font-weight: 700;
        color: #5a6bb0;
        letter-spacing: 0.05em;
    }
    
    .ticker-title {
        color: #1f2a44;
    }
    
    .ticker-item:hover .ticker-title {
        color: #243b80;
        text-decoration: underline;
    }
    
    .ticker-link {
        font-weight: 600;
        color: #4c6ef5;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
    }
    
    .ticker-link:hover {
        text-decoration: underline;
    }
    
    @keyframes tickerScrollY {
        0% { transform: translateY(0); }
        100% { transform: translateY(-50%); }
    }
    
    .btn-secondary {
        background: var(--gradient-secondary);
        color: white;
        box-shadow: var(--shadow-light);
    }
    
    .btn-secondary:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--shadow-medium);
        color: white;
    }
    
    .btn-accent {
        background: var(--gradient-accent);
        color: white;
        box-shadow: var(--shadow-light);
    }
    
    .btn-accent:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--shadow-medium);
        color: white;
    }
    
    /* Language switch */
    .language-switch {
        position: absolute;
        top: 1rem;
        right: 1rem;
        display: flex;
        gap: 0.5rem;
    }
    
    .lang-btn {
        padding: 0.5rem 1rem;
        border: 2px solid var(--border-color);
        background: white;
        color: var(--text-color);
        text-decoration: none;
        border-radius: 9999px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .lang-btn:hover,
    .lang-btn.active {
        background: var(--gradient-secondary);
        color: white;
        border-color: transparent;
        transform: translateY(-2px);
        box-shadow: var(--shadow-light);
    }
    
    .lang-btn::after {
        display: none;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-section {
            padding: 2rem 1rem 2.5rem;
            margin: 1rem auto 1.25rem;
            min-height: auto;
        }
        
        .hero-title {
            font-size: 2.6rem;
        }
        
        .hero-subtitle {
            font-size: 1.15rem;
            text-align: center;
        }
        
        .hero-ticker {
            flex-direction: column;
            align-items: stretch;
            gap: 0.75rem;
            border-radius: 24px;
            width: 100%;
        }
        
        .ticker-track,
        .ticker-inner {
            flex-direction: column;
            gap: 0.75rem;
            animation: none;
        }
        
        .ticker-track::before,
        .ticker-track::after {
            display: none;
        }
        
        .ticker-item {
            white-space: normal;
        }
        
        .language-switch {
            position: static;
            justify-content: center;
            margin: 1rem 0;
        }
    }
    
    @media (max-width: 480px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
            text-align: center;
        }
        
        .hero-ticker {
            padding: 1rem;
        }
    }
</style>

<div class="hero-section">
    <h1 class="hero-title">Functional Genomics Lab @ CPU</h1>
    <p class="hero-subtitle">Welcome to our research laboratory focused on understanding genome function through cutting-edge functional genomics approaches.</p>
</div>

<!-- News Ticker moved below hero -->
{% assign news_page = site.pages | where: "path", "news.md" | first %}
{% if news_page and news_page.news_items and news_page.news_items.size > 0 %}
<div class="hero-ticker">
    <span class="ticker-label">What's New</span>
    <div class="ticker-track">
        <div class="ticker-inner">
            {% for item in news_page.news_items limit: 4 %}
            <a class="ticker-item" href="/news/">
                <span class="ticker-date">{{ item.date }}</span>
                <span class="ticker-title">{{ item.title }}</span>
            </a>
            {% endfor %}
            {% for item in news_page.news_items limit: 4 %}
            <a class="ticker-item" href="/news/">
                <span class="ticker-date">{{ item.date }}</span>
                <span class="ticker-title">{{ item.title }}</span>
            </a>
            {% endfor %}
        </div>
    </div>
    <a class="ticker-link" href="/news/">View all →</a>
</div>
{% endif %}

<!-- Language Switch -->
<div class="language-switch">
    <a href="/" class="lang-btn active">English</a>
    <a href="/cn/" class="lang-btn">中文</a>
</div>
