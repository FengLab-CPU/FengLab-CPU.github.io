---
layout: default
title: Yuanqing Feng · Profile
lang: en
permalink: /people/yuanqing-feng/
---

<style>
  .profile-page {
    max-width: 1200px;
    margin: 2rem auto 3rem;
    padding: 0 2rem;
    box-sizing: border-box;
  }

  .profile-header {
    margin-bottom: 1.8rem;
  }

  .profile-name {
    font-size: 2.3rem;
    font-weight: 700;
    color: var(--heading-color);
    margin: 0 0 0.4rem;
    letter-spacing: -0.03em;
  }

  .profile-title {
    font-size: 1.1rem;
    color: var(--heading-secondary);
    font-weight: 600;
    margin-bottom: 0.25rem;
  }

  .profile-position {
    font-size: 0.98rem;
    color: var(--text-muted);
  }

  .profile-layout {
    display: flex;
    align-items: flex-start;
    gap: 2rem;
  }

  .profile-photo {
    flex: 0 0 260px;
    max-width: 260px;
  }

  .profile-photo-inner {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow-light);
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  }

  .profile-photo img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .profile-content {
    flex: 1;
    min-width: 0;
  }

  .profile-tagline {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--heading-secondary);
    padding: 0.85rem 1.1rem;
    background: var(--background-subtle);
    border-radius: 12px;
    border-left: 4px solid var(--heading-secondary);
    margin: 0 0 1.6rem;
  }

  .profile-contact {
    margin-top: 0.5rem;
    font-size: 0.95rem;
    color: var(--text-muted);
  }

  .profile-contact a {
    font-weight: 600;
  }

  .section-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--heading-secondary);
    margin: 1.6rem 0 0.85rem;
    padding-bottom: 0.35rem;
    border-bottom: 2px solid rgba(44, 95, 45, 0.25);
  }

  .timeline {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .timeline-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 0.85rem;
  }

  .timeline-period {
    flex: 0 0 96px;
    font-weight: 600;
    color: var(--heading-secondary);
  }

  .timeline-detail {
    flex: 1;
  }

  .timeline-detail strong {
    color: var(--text-color);
  }

  .research-list {
    margin: 0;
    padding-left: 1.2rem;
  }

  .research-list li {
    margin-bottom: 0.35rem;
  }

  .profile-intro {
    font-size: 0.98rem;
    line-height: 1.9;
    color: var(--text-color);
  }

  .awards-list,
  .service-list {
    margin: 0;
    padding-left: 1.2rem;
  }

  .awards-list li,
  .service-list li {
    margin-bottom: 0.4rem;
  }

  .profile-link {
    font-weight: 600;
  }

  @media (max-width: 900px) {
    .profile-layout {
      gap: 1.5rem;
    }
  }

  @media (max-width: 768px) {
    .profile-page {
      padding: 0 1.25rem;
    }

    .profile-layout {
      flex-direction: column;
      align-items: stretch;
    }

    .profile-photo {
      max-width: 260px;
      margin: 0 auto;
      width: 100%;
    }

    .profile-header {
      text-align: center;
    }

    .profile-tagline {
      text-align: center;
    }
  }

  @media (max-width: 480px) {
    .profile-page {
      padding: 0 1rem;
      margin-top: 1.5rem;
    }

    .profile-name {
      font-size: 2rem;
    }
  }
</style>

<div class="profile-page">
  <div class="profile-header">
    <div class="profile-name">Yuanqing Feng</div>
    <div class="profile-title">Professor · Ph.D. Advisor</div>
    <div class="profile-position">Principal Investigator, Functional Genomics Laboratory, China Pharmaceutical University</div>
    <div class="profile-contact">
      Email:
      <a href="mailto:fengyuanqing2010@gmail.com">fengyuanqing2010@gmail.com</a>
      · Google Scholar:
      <a href="https://scholar.google.com/citations?user=nWYWiVUAAAAJ" target="_blank" rel="noopener" class="profile-link">View publications</a>
    </div>
  </div>

  <div class="profile-layout">
    <div class="profile-photo">
      <div class="profile-photo-inner">
        <img src="{{ '/assets/images/me.jpg' | relative_url }}" alt="Yuanqing Feng">
      </div>
    </div>

    <div class="profile-content">
      <div class="profile-tagline">
        Genetic variation · Population genetics · Functional genomics · Precision medicine
      </div>

      <h2 class="section-title">Short Bio</h2>
      <p class="profile-intro">
        My research focuses on the genetic and evolutionary basis of human phenotypic diversity and disease susceptibility, with a particular interest in how non-coding variants regulate gene
        expression and influence complex traits and disease risk. By integrating population genetics, functional genomics, and computational analysis, I aim to build causal links from genetic
        variation to molecular function, cellular states, and organismal phenotypes, thereby elucidating the genetic architecture of human traits and diseases. My work spans topics such as skin
        pigmentation evolution, cardiac energy metabolism, immunity, and infectious diseases, and has led to first-author publications in journals including
        <em>Nature Genetics</em>, <em>PNAS</em>, <em>Molecular Biology and Evolution</em>, and <em>Circulation</em>.
        I was invited to give a Plenary Talk at ASHG 2022 and received the Chan Zuckerberg Initiative Next Generation Researcher Award in 2023.
      </p>

      <h2 class="section-title">Research Interests</h2>
      <ul class="research-list">
        <li>Population genetics of human phenotypic diversity</li>
        <li>Functional genomics and systematic characterization of non-coding variants</li>
        <li>Human adaptation and natural selection in diverse populations</li>
        <li>Genetic mechanisms underlying complex diseases (e.g., cardiovascular and immune-related diseases)</li>
      </ul>

      <h2 class="section-title">Education</h2>
      <ul class="timeline">
        <li class="timeline-item">
          <div class="timeline-period">2011–2017</div>
          <div class="timeline-detail">
            <strong>Ph.D. in Molecular Medicine</strong><br>
            Peking University (Advisor: Prof. Ruiping Xiao)
          </div>
        </li>
        <li class="timeline-item">
          <div class="timeline-period">2007–2011</div>
          <div class="timeline-detail">
            <strong>B.S. in Pharmaceutical Engineering</strong><br>
            Jilin University
          </div>
        </li>
      </ul>

      <h2 class="section-title">Research and Professional Experience</h2>
      <ul class="timeline">
        <li class="timeline-item">
          <div class="timeline-period">2025–Present</div>
          <div class="timeline-detail">
            <strong>Professor (Ph.D. Advisor)</strong><br>
            China Pharmaceutical University
          </div>
        </li>
        <li class="timeline-item">
          <div class="timeline-period">2023–2025</div>
          <div class="timeline-detail">
            <strong>Research Associate</strong><br>
            University of Pennsylvania
          </div>
        </li>
        <li class="timeline-item">
          <div class="timeline-period">2018–2023</div>
          <div class="timeline-detail">
            <strong>Postdoctoral Fellow</strong><br>
            University of Pennsylvania
          </div>
        </li>
        <li class="timeline-item">
          <div class="timeline-period">2017–2018</div>
          <div class="timeline-detail">
            <strong>Postdoctoral Fellow</strong><br>
            Peking University
          </div>
        </li>
      </ul>

      <h2 class="section-title">Honors and Awards</h2>
      <ul class="awards-list">
        <li>2023 &mdash; Chan Zuckerberg Initiative Next Generation Researcher Award</li>
        <li>2023 &mdash; Advanced Gene Mapping Course Award, Rockefeller University</li>
        <li>2016 &mdash; National Graduate Scholarship, Peking University</li>
        <li>2015 &mdash; President’s Scholarship, Peking University</li>
      </ul>

      <h2 class="section-title">Selected Talks and Service</h2>
      <ul class="service-list">
        <li>2022 &mdash; Plenary Talk, American Society of Human Genetics (ASHG) Annual Meeting</li>
        <li>Multiple presentations at Chan Zuckerberg Initiative Single-Cell Biology Annual Meetings (2021–2023)</li>
        <li>Attended Biology of Genomes, Cold Spring Harbor Laboratory (2020)</li>
        <li>Regular participation in ASHG Annual Meetings (2019–2022)</li>
        <li>Reviewer for journals including <em>Science</em>, <em>Nature Communications</em>, <em>PNAS</em>, and <em>AJHG</em></li>
      </ul>
    </div>
  </div>
</div>

