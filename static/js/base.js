function toggleSubmenu(menuId) {
    // Hide all submenus
    document.querySelectorAll('.submenu').forEach(menu => menu.style.display = 'none');

    // Show the secondary sidebar
    const secondarySidebar = document.getElementById('secondarySidebar');
    secondarySidebar.style.display = 'block';

    // Show the selected submenu
    const selectedMenu = document.getElementById(menuId);
    if (selectedMenu) {
        selectedMenu.style.display = 'block';
    }

    // Adjust main content width
    const contentContainer = document.querySelector('.content-container');
    contentContainer.classList.add('with-secondary-sidebar');

    // Remove 'active' class from all links
    document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));

    // Add 'active' class to the selected link
    event.currentTarget.classList.add('active');
}
