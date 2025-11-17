---
layout: default
title: News
permalink: /news/
news_items:
  - date: "APR 2026"
    title: "Joined China Pharmaceutical University"
    excerpt: "Started as Professor (Ph.D. Advisor) at China Pharmaceutical University in April 2026."
    category: "position"
  - date: "FEB 2024"
    title: "Nature Genetics Publication"
    excerpt: 'Our paper "Integrative functional genomic analyses identify genetic variants influencing skin pigmentation in Africans" was published in Nature Genetics.'
    link: "https://pubmed.ncbi.nlm.nih.gov/38200130/"
    pmid: "38200130"
    category: "publication"
  - date: "NOV 2023"
    title: "Next Generation Scientist Award"
    excerpt: "Received the Next Generation Scientist Award from Chan Zuckerberg Initiative."
    category: "award"
  - date: "AUG 2023"
    title: "New Position at CPU"
    excerpt: "Started as Research Associate at China Pharmaceutical University."
    category: "position"
  - date: "MAR 2023"
    title: "Cell Publication"
    excerpt: 'Our paper "Whole-genome sequencing reveals a complex African population demographic history" was published in Cell.'
    link: "https://pubmed.ncbi.nlm.nih.gov/36868214/"
    pmid: "36868214"
    category: "publication"
  - date: "OCT 2022"
    title: "ASHG 2022 Presentation"
    excerpt: "Presented our research on African genomics at the ASHG 2022 Annual Meeting."
    category: "presentation"
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

    .news-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0.5rem 2rem;
        box-sizing: border-box;
    }

    .news-header {
        text-align: center;
        margin-top: 0.1rem;
        margin-bottom: 0.8rem;
        padding: 0.8rem;
        background: transparent;
        border-radius: 16px;
        color: inherit;
        box-shadow: none;
    }

    .news-title {
        font-size: 2rem;
        margin-top: 0.1rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
        color: var(--heading-color);
    }

    .news-section {
        margin: 2rem 0;
    }

    .news-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .news-item {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .news-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--gradient-accent);
    }

    .news-item:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
        border-color: rgba(115, 93, 165, 0.2);
    }

    .news-date {
        font-size: 0.9rem;
        color: var(--accent-color);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }

    .news-category {
        display: inline-block;
        background: var(--gradient-accent);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }

    .news-category.publication {
        background: var(--gradient-secondary);
    }

    .news-category.award {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
    }

    .news-category.position {
        background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
    }

    .news-category.presentation {
        background: linear-gradient(135deg, #fd7e14 0%, #e55100 100%);
    }

    .news-item-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--secondary-color);
        margin-bottom: 0.8rem;
        line-height: 1.4;
    }

    .news-excerpt {
        font-size: 1rem;
        color: var(--text-light);
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .news-links {
        display: flex;
        gap: 1rem;
        align-items: center;
    }

    .pmid-link {
        color: var(--accent-color);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: color 0.3s ease;
    }

    .pmid-link:hover {
        color: var(--primary-color);
        text-decoration: underline;
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

    /* Responsive Design */
    @media (max-width: 768px) {
        .news-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .news-title {
            font-size: 2rem;
        }
        
        .news-header {
            padding: 1.5rem;
        }
        
        .news-item {
            padding: 1.2rem;
        }
    }

    @media (max-width: 480px) {
        .news-container {
            padding: 1rem 0.5rem;
        }
        
        .news-header {
            padding: 1rem;
        }
        
        .news-title {
            font-size: 1.8rem;
        }
        
        .news-grid {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
        
        .news-item {
            padding: 1rem;
        }
        
        .news-item-title {
            font-size: 1.1rem;
        }
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
</style>

<div class="news-container">
    <div class="news-header fade-in">
        <h1 class="news-title">News and Updates</h1>
    </div>
    <div class="news-section">
        <div class="news-grid">
            {% for item in page.news_items %}
            <div class="news-item fade-in">
                <div class="news-date">{{ item.date }}</div>
                {% if item.category %}
                <span class="news-category {{ item.category }}">{{ item.category }}</span>
                {% endif %}
                <div class="news-item-title">{{ item.title }}</div>
                <div class="news-excerpt">{{ item.excerpt }}</div>
                {% if item.link %}
                <div class="news-links">
                    <a href="{{ item.link }}" class="pmid-link" target="_blank" rel="noopener noreferrer">PMID: {{ item.pmid }}</a>
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        
        <div style="text-align: center; margin-top: 3rem;">
            <a href="/" class="back-link">
                <i class="fas fa-home"></i>
                Back to Homepage
            </a>
        </div>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const fadeElements = document.querySelectorAll('.fade-in');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, index * 100);
                }
            });
        }, { threshold: 0.1 });

        fadeElements.forEach(el => observer.observe(el));
    });
</script>
