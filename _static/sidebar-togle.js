document.addEventListener('DOMContentLoaded', function() {
    const sidebarButton = document.createElement('button');
    sidebarButton.id = 'toggle-secondary-sidebar';
    sidebarButton.textContent = 'Toggle Page TOC';

    const navbar = document.querySelector('.navbar-nav');
    if (navbar) {
        navbar.appendChild(sidebarButton);
    }

    // Set initial state for all pages
    const sidebar = document.querySelector('.bd-sidebar-secondary');

    // If there's no sidebar at all, add the sidebar-hidden class immediately
    if (!sidebar) {
        document.body.classList.add('sidebar-hidden');
    }
    // If there is a sidebar but it's hidden, add the class
    else if (sidebar.style.display === 'none' || getComputedStyle(sidebar).display === 'none') {
        document.body.classList.add('sidebar-hidden');
    }

    sidebarButton.addEventListener('click', function() {
        const sidebar = document.querySelector('.bd-sidebar-secondary');
        if (sidebar) {
            if (sidebar.style.display === 'none' || !sidebar.style.display) {
                sidebar.style.display = 'block';
                document.body.classList.remove('sidebar-hidden');
            } else {
                sidebar.style.display = 'none';
                document.body.classList.add('sidebar-hidden');
            }
        }
    });

    // Hide the toggle button if there's no secondary nav
    if (!sidebar) {
        sidebarButton.style.display = 'none';
    }
});