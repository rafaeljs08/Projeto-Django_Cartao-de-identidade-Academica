(function () {
    'use strict';

    var toggleBtn = document.getElementById('toggle-nav-sidebar');
    var sidebar = document.getElementById('nav-sidebar');
    var overlay = document.getElementById('fepi-sidebar-overlay');

    if (!toggleBtn || !sidebar) {
        return;
    }

    function closeSidebar() {
        document.body.classList.remove('fepi-sidebar-open');
    }

    function openSidebar() {
        document.body.classList.add('fepi-sidebar-open');
    }

    toggleBtn.addEventListener('click', function () {
        if (document.body.classList.contains('fepi-sidebar-open')) {
            closeSidebar();
        } else {
            openSidebar();
        }
    });

    if (overlay) {
        overlay.addEventListener('click', closeSidebar);
    }

    window.addEventListener('resize', function () {
        if (window.innerWidth > 1024) {
            closeSidebar();
        }
    });
})();
