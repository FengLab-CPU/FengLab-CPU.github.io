---
layout: default
title: 团队成员
permalink: /cn/people/
---

<style>
    .people-container {
        margin: 0 auto;
        padding: 2rem 2rem;
        width: 100%;
        max-width: 1200px;
        box-sizing: border-box;
    }

    .section-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--heading-color);
        text-align: center;
        margin-top: 0.1rem;
        margin-bottom: 0.5rem;
        padding-bottom: 0;
        border-bottom: none;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        letter-spacing: -0.3px;
    }

    .section-title::after {
        content: '';
        display: block;
        width: clamp(80px, 25vw, 360px);
        height: 4px;
        background: var(--gradient-primary);
        border-radius: 2px;
        margin: 0.6rem auto 0;
    }

    .people-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.36rem;
        margin-bottom: 3rem;
        width: 100%;
        box-sizing: border-box;
        background: var(--background-subtle);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1rem;
    }

    .person-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 12px;
        padding: 0.75rem;
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        box-shadow: var(--shadow-light);
        min-height: 168px;
        transform: scale(0.75);
        transform-origin: center;
    }

    .person-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-vibrant);
        border-color: rgba(44, 95, 45, 0.2);
    }

    .person-photo {
        width: clamp(140px, 65%, 240px);
        aspect-ratio: 5 / 7;
        border-radius: 0;
        margin: 0 auto 0.45rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 0.6px solid var(--border-color);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        color: var(--primary-color);
        transition: all 0.3s ease;
    }

    .person-card:hover .person-photo {
        border-color: var(--secondary-color);
        transform: scale(1.05);
    }

    .person-name {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2f4f4f;
        margin-bottom: 0.3rem;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        letter-spacing: -0.3px;
    }

    .person-title {
        font-size: 1.05rem;
        color: var(--primary-color);
        margin-bottom: 0.18rem;
        font-weight: 500;
    }

    .person-contact {
        font-size: 0.9rem;
        color: var(--heading-accent);
    }

    .person-contact a {
        color: var(--link-color);
        text-decoration: none;
        transition: color 0.3s ease;
        font-weight: 500;
    }

    .person-contact a:hover {
        color: #2f4f4f;
        text-decoration: underline;
    }

    .alumni-section {
        background: var(--background-subtle);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 3rem;
    }

    .alumni-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 1rem;
    }

    .alumni-table th,
    .alumni-table td {
        padding: 0.75rem 1rem;
        text-align: left;
        border-bottom: 1px solid var(--border-color);
    }

    .alumni-table th {
        background: #ffffff;
        font-weight: 600;
        color: #2f4f4f;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        letter-spacing: -0.3px;
    }

    .alumni-table tr:hover {
        background: #ffffff;
    }

    .alumni-table td {
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #36454f;
    }

    .year-cell {
        font-weight: 500;
        color: #2C5F2D;
        white-space: nowrap;
    }

    .current-cell {
        color: #708090;
        font-style: italic;
    }

    @media (max-width: 768px) {
        .people-container {
            padding: 1.5rem 1rem;
        }

        .people-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
        }
    }

    @media (max-width: 480px) {
        .people-grid {
            grid-template-columns: 1fr;
        }
    }
</style>

<div class="people-container">
    <div class="lab-section">
        <h2 class="section-title">在职成员</h2>
        <div class="people-grid">
            <div class="person-card">
                <div class="person-photo">
                    <img src="/assets/images/me.jpg" alt="冯园庆" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div class="person-info">
                    <div class="person-name">冯园庆</div>
                    <div class="person-title">课题负责人（PI）</div>
                </div>
            </div>

            <div class="person-card">
                <div class="person-photo">👩‍🎓</div>
                <div class="person-info">
                    <div class="person-name">研究生 1</div>
                    <div class="person-title">博士研究生</div>
                </div>
            </div>

            <div class="person-card">
                <div class="person-photo">👨‍🎓</div>
                <div class="person-info">
                    <div class="person-name">研究生 2</div>
                    <div class="person-title">博士研究生</div>
                </div>
            </div>

            <div class="person-card">
                <div class="person-photo">👩‍🔬</div>
                <div class="person-info">
                    <div class="person-name">博士后</div>
                    <div class="person-title">博士后研究员</div>
                </div>
            </div>

            <div class="person-card">
                <div class="person-photo">👨‍💻</div>
                <div class="person-info">
                    <div class="person-name">科研助理</div>
                    <div class="person-title">研究专员</div>
                </div>
            </div>

            <div class="person-card">
                <div class="person-photo">👩‍🔬</div>
                <div class="person-info">
                    <div class="person-name">本科生</div>
                    <div class="person-title">本科科研助理</div>
                </div>
            </div>
        </div>
    </div>

    <div class="alumni-section">
        <h2 class="section-title">毕业成员（示例）</h2>
        <table class="alumni-table">
            <thead>
                <tr>
                    <th>姓名</th>
                    <th>在组身份</th>
                    <th>年份</th>
                    <th>目前去向</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>示例校友 1</strong></td>
                    <td>博士研究生</td>
                    <td class="year-cell">2023</td>
                    <td class="current-cell">博士后，某高校</td>
                </tr>
                <tr>
                    <td><strong>示例校友 2</strong></td>
                    <td>研究专员</td>
                    <td class="year-cell">2020</td>
                    <td class="current-cell">生物技术公司高级科学家</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
