// Amploi — scripts du site
document.addEventListener('DOMContentLoaded', () => {
    // En-tête : ombre au défilement
    const header = document.querySelector('.site-header');
    const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 8);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    // Menu mobile
    const toggle = document.querySelector('.menu-toggle');
    const closeMenu = () => {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
    };
    toggle.addEventListener('click', () => {
        const open = document.body.classList.toggle('nav-open');
        toggle.setAttribute('aria-expanded', String(open));
    });
    document.querySelectorAll('.main-nav a').forEach(a => a.addEventListener('click', closeMenu));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });

    // Apparition au défilement
    const reveals = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    io.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        reveals.forEach(el => io.observe(el));
    } else {
        reveals.forEach(el => el.classList.add('is-visible'));
    }

    // Compteurs animés
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    document.querySelectorAll('[data-count]').forEach(el => {
        if (reduceMotion) return;
        const target = parseInt(el.dataset.count, 10);
        const prefix = el.dataset.prefix || '';
        const start = performance.now();
        const duration = 1200;
        const tick = now => {
            const t = Math.min((now - start) / duration, 1);
            el.textContent = prefix + Math.round(target * (1 - Math.pow(1 - t, 3)));
            if (t < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
    });

    // Année du pied de page
    document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

    // Filtres du blog
    const filters = document.querySelectorAll('.filter');
    filters.forEach(btn => {
        btn.addEventListener('click', () => {
            const cat = btn.dataset.filter;
            filters.forEach(b => b.classList.toggle('is-active', b === btn));
            document.querySelectorAll('#post-list .post-card').forEach(card => {
                card.hidden = cat !== 'all' && card.dataset.cat !== cat;
            });
        });
    });

    // Partage d'article
    const share = document.querySelector('.share');
    if (share) {
        const url = window.location.href;
        const text = `À lire sur Amploi : ${share.dataset.title}`;
        const links = {
            whatsapp: `https://wa.me/?text=${encodeURIComponent(text + ' ' + url)}`,
            linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`,
            facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`
        };
        share.querySelectorAll('a[data-share]').forEach(a => { a.href = links[a.dataset.share]; });

        const copyBtn = share.querySelector('[data-share="copy"]');
        copyBtn.addEventListener('click', async () => {
            const label = copyBtn.querySelector('span');
            try {
                await navigator.clipboard.writeText(url);
                label.textContent = 'Lien copié !';
            } catch {
                label.textContent = 'Copie impossible';
            }
            setTimeout(() => { label.textContent = 'Copier le lien'; }, 2000);
        });
    }
});
