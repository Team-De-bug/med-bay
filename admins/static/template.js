var sidebarIsClosed = false;

var xhttp = new XMLHttpRequest();

function closeSidebar() {
    var navItems = document.getElementsByClassName("nav-link");
    //if the sidebar is not closed
    if (!sidebarIsClosed) {
        //then we close the sidebar
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('side-bar-title').style.opacity = "0%";
        document.getElementById('side-bar-title').style.fontSize = "0vw";
        for (var i = 0; i < navItems.length; i++) {
            navItems.item(i).style.opacity = "0%";
            navItems.item(i).style.fontSize = "0vw";
        }
        sidebarIsClosed = true;
    } else {
        //we open the sidebar
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('side-bar-title').style.opacity = "100%";
        document.getElementById('side-bar-title').style.fontSize = "1.75vw";
        for (i = 0; i < navItems.length; i++) {
            navItems.item(i).style.display = "block";
            navItems.item(i).style.opacity = "100%";
            navItems.item(i).style.fontSize = "1.5vw";
        }
        sidebarIsClosed = false;
    }
}

function showLogo() {    
    closeSidebar();

    if (sessionStorage.getItem('newSession') === null) {
        document.getElementById("loadLogo").style.display = "flex";
        document.getElementById("loadLogoImg").style.opacity = "100%";
        $(".root-grid").css("display", "none");
        setTimeout(function () { document.getElementById("loadLogoImg").style.opacity = "0"; }, 3000);
        setTimeout(function() {$(".root-grid").css("display", "inline-grid"); }, 3000);
        setTimeout(function () {document.getElementById("loadLogo").style.opacity = "0"; }, 5000);
        setTimeout(function () {document.getElementById("loadLogo").style.display = "none"; }, 6000);
        sessionStorage.setItem('newSession', 'false');
    } else {
        document.getElementById("loadLogo").style.display = "none";
    }
}

function showMessage(message) {
    alert(message);
}

function copyDetail(detailId) {
    var copyID = document.getElementById(detailId);
    copyID.select();
    copyID.setSelectionRange(0, 99999)
    document.execCommand("copy");
    showMessage("Copied Pateint Detail: " + copyID.value);
}

function switchTheme() {

    $.ajax({

        url: "/set_theme",

    });
}

function getCookie(name) {
    function escape(s) { return s.replace(/([.*+?\^$(){}|\[\]\/\\])/g, '\\$1'); }
    var match = document.cookie.match(RegExp('(?:^|;\\s*)' + escape(name) + '=([^;]*)'));
    return match ? match[1] : null;
}

function toggleTheme() {

    sessionStorage.setItem('toggle', 'true');
    if (sessionStorage.getItem('toggle') === 'true') {

        $("#loadLogo").css("opacity", "0");
        $("#loadLogo").css("display", "flex");
        setTimeout(function () { $("#loadLogo").css("opacity", "100%"); }, 1000);
        setTimeout(function () { $("#loadLogoImg").css("opacity", "100%"); }, 1000);
        if (getCookie("theme") === "w") {
            console.log("change to dark");
            setTimeout(function () { $("#loadLogo").css("backgroundColor", "#231b31"); }, 1000);
        } else if (getCookie("theme") === "d") {
             console.log("change to light");
            setTimeout(function () { $("#loadLogo").css("backgroundColor", "#E00043"); },1000);
        }
        setTimeout(function () { $("#loadLogoImg").css("opacity", "0"); }, 3000);
        setTimeout(function () { $("#loadLogo").css("opacity", "0"); }, 5000);
        setTimeout(function () { $("#loadLogo").css("display", "none"); }, 6000);
        sessionStorage.setItem('toggle', 'false');
        switchTheme();
        setTimeout(function() {location.reload();}, 4900);
    }
}