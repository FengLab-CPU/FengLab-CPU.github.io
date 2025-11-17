---
layout: default
title: 招聘
permalink: /cn/jobs/
---

<style>
    :root {
        --primary-color: #2C5F2D;
        --secondary-color: #1E2761;
        --accent-color: #735DA5;
        --gradient-primary: linear-gradient(135deg, #2C5F2D 0%, #31473A 100%);
        --gradient-secondary: linear-gradient(135deg, #1E2761 0%, #2C3E6E 100%);
        --text-dark: #2D3748;
        --text-light: #4A5568;
        --bg-light: #F7FAFC;
        --border-color: #E2E8F0;
    }

    .jobs-container {
        margin: 0 auto;
        padding: 0.5rem 2rem;
        max-width: 1200px;
        box-sizing: border-box;
    }

    .jobs-header {
        text-align: center;
        margin-top: 0.1rem;
        margin-bottom: 0.2rem;
        padding: 0.8rem;
        background: transparent;
        border-radius: 16px;
        color: inherit;
        box-shadow: none;
    }

    .jobs-title {
        font-size: 2.5rem;
        margin-top: 0.1rem;
        margin-bottom: 0.8rem;
        font-weight: 700;
        color: var(--heading-color);
    }

    .jobs-subtitle {
        font-size: 1.05rem;
        opacity: 0.9;
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.6;
        color: var(--text-light);
    }

    .jobs-section {
        margin: 2rem 0;
    }

    .jobs-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .job-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .job-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--gradient-accent);
    }

    .job-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
        border-color: rgba(115, 93, 165, 0.2);
    }

    .job-title {
        font-size: 1.4rem;
        color: var(--secondary-color);
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .job-type {
        display: inline-block;
        background: var(--gradient-accent);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    .job-description {
        font-size: 1rem;
        color: var(--text-light);
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }

    .job-requirements {
        margin-bottom: 1.5rem;
    }

    .job-requirements h4 {
        color: var(--primary-color);
        font-size: 1rem;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .job-requirements ul {
        list-style: none;
        padding-left: 0;
        margin: 0;
    }

    .job-requirements li {
        position: relative;
        padding-left: 1.5rem;
        margin-bottom: 0.5rem;
        font-size: 0.95rem;
        color: var(--text-dark);
    }

    .job-requirements li::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: var(--accent-color);
        font-weight: bold;
    }

    .application-info {
        background: var(--bg-light);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid var(--primary-color);
        margin-bottom: 1.5rem;
    }

    .application-info h4 {
        color: var(--primary-color);
        font-size: 1rem;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }

    .application-info p {
        font-size: 0.95rem;
        color: var(--text-dark);
        line-height: 1.5;
        margin-bottom: 0.5rem;
    }

    .contact-email {
        color: var(--accent-color);
        text-decoration: none;
        font-weight: 500;
    }

    .contact-email:hover {
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

    .no-positions {
        text-align: center;
        padding: 3rem;
        background: var(--bg-light);
        border-radius: 16px;
        border: 2px dashed var(--border-color);
    }

    .no-positions h3 {
        color: var(--text-dark);
        margin-bottom: 1rem;
    }

    .no-positions p {
        color: var(--text-light);
        max-width: 600px;
        margin: 0 auto;
    }

    @media (max-width: 768px) {
        .jobs-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
    }

    @media (max-width: 480px) {
        .jobs-container {
            padding: 1rem 0.75rem;
        }
    }
</style>

<div class="jobs-container">
    <div class="jobs-header">
        <h1 class="jobs-title">加入我们团队</h1>
        <p class="jobs-subtitle">
            欢迎功能基因组学及相关领域的优秀人才加入或合作，共探新方向。
        </p>
    </div>

    <div class="jobs-section">
        <div class="jobs-grid">
            <div class="job-card">
                <h3 class="job-title">博士后 / 研究员</h3>
                <span class="job-type">全职</span>
                <p class="job-description">
                    功能基因组学和人类遗传学相关领域。
                </p>

                <div class="job-requirements">
                    <h4>岗位要求：</h4>
                    <ul>
                        <li><strong>教育背景：</strong>遗传学、分子生物学、生物信息学或相关领域博士学位。</li>
                        <li><strong>科研经验：</strong>有功能基因组学实验经验（如CRISPR筛选等）者优先。</li>
                        <li><strong>技术能力：</strong>熟练掌握Python/R等编程语言，具备数据分析能力。</li>
                        <li><strong>学术成果：</strong>有高质量论文发表记录。</li>
                        <li><strong>综合素质：</strong>良好的沟通能力与团队合作精神。</li>
                    </ul>
                </div>

                <div class="application-info">
                    <h4>岗位待遇：</h4>
                    <p>1. 聘为“中国药科大学兴药科研博士后”，年薪<span style="font-weight:600;">30万元人民币起</span>；</p>
                    <p>2. 享受公费医疗、公积金及校工会相关福利待遇。</p>
                </div>

                <div class="application-info">
                    <h4>职业发展：</h4>
                    <p>1. 在站期间取得突出科研成果者，可申报学校特聘副研究员或具有正式编制的副教授 / 副研究员等长期职位；</p>
                    <p>2. 支持依托中国药科大学申请国家资助博士后研究人员计划（12–28万元/年）、国家自然科学基金（约30万元/项目）、江苏省自然科学基金（约20万元/项目）、江苏省卓越博士后计划（10–25万元/年）等各类项目，所有渠道的工资及经费待遇可叠加发放，上不封顶；</p>
                    <p>3. 工作地点：南京市江宁校区。</p>
                </div>
            </div>

            <div class="job-card">
                <h3 class="job-title">研究生</h3>
                <span class="job-type">全职/轮转</span>
            <p class="job-description">
                欢迎对功能基因组学或人类遗传学感兴趣的研究生加入课题组，开展实验与计算相结合的交叉研究。
            </p>

            <div class="job-requirements">
                <h4>岗位要求：</h4>
                <ul>
                    <li>相关专业在读或即将入学的研究生</li>
                    <li>对基因组学与人类疾病研究有浓厚兴趣</li>
                    <li>具备一定编程或数据分析基础者优先</li>
                    <li>具有主动学习能力和独立科研潜力</li>
                </ul>
            </div>
            </div>
        </div>

        <div class="no-positions" style="margin-top: 2rem;">
            <h3>其他机会</h3>
            <p>
                欢迎有意加入或合作的朋友发送邮件联系。
            </p>
            <p><a href="mailto:fengyuanqing2010@gmail.com" class="contact-email">fengyuanqing2010@gmail.com</a></p>
        </div>

        <div style="text-align: center; margin-top: 3rem;">
            <a href="/cn/" class="back-link">
                <i class="fas fa-home"></i>
                返回主页
            </a>
        </div>
    </div>
</div>
