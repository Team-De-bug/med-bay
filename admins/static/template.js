var sidebarIsClosed = false;

function closeSidebar() {
    var navItems = document.getElementsByClassName("nav-link");
    //if the sidebar is not closed
    if(!sidebarIsClosed){
        //then we close the sidebar
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('side-bar-title').style.opacity="0%";
        document.getElementById('side-bar-title').style.fontSize="0vw";
        for (i = 0; i < navItems.length; i++) {
            navItems.item(i).style.opacity="0%";
            navItems.item(i).style.fontSize="0vw";
        }
        sidebarIsClosed = true;
    } else {
        //we open the sidebar
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('side-bar-title').style.opacity="100%";
        document.getElementById('side-bar-title').style.fontSize="1.75vw";
        for (i = 0; i < navItems.length; i++) {
            navItems.item(i).style.opacity="100%";
            navItems.item(i).style.fontSize="1.5vw";
        }
        sidebarIsClosed = false;
    }
}