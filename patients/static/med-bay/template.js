var sidebarIsClosed = false;
function closeSidebar() {
    if(!sidebarIsClosed){
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('side-bar-title').style.display="none";
        sidebarIsClosed = true;
    } else {
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('side-bar-title').style.display= "block";
        sidebarIsClosed = false;
    }
}