document.addEventListener("DOMContentLoaded", () => {
    const cursor = document.getElementById("cursor");
    const buttons = document.querySelectorAll(".page");
    const title = document.querySelector(".title");

    // Cursor
    document.addEventListener("mousemove", e => {
        cursor.style.left = e.pageX + "px";
        cursor.style.top = e.pageY + "px";
    });

    // Page navigation
    window.openPage = function(num) { window.location.href = `page${num}.html`; }
    window.goHome = function() { window.location.href = "index.html"; }

    // Apply config
    window.applyPageConfig = function(pageNum){
        if(!window.pageConfigs) return;
        const cfg = window.pageConfigs[pageNum];
        if(cfg){
            document.body.style.background = `linear-gradient(180deg,${cfg.bgStart},${cfg.bgEnd})`;
            if(title){
                title.style.color = cfg.glow;
                title.style.textShadow = `0 0 20px ${cfg.glow}, 0 0 40px ${cfg.glow}`;
            }
        }
    }

    // Circle fish orbit
    let angle = 0;
    function moveFish(){
        const radius = 150;
        angle += 0.02;
        buttons.forEach((btn, i) => {
            const a = angle + (i * (Math.PI * 2 / buttons.length));
            btn.style.left = `${50 + radius * Math.cos(a)}px`;
            btn.style.top = `${50 + radius * Math.sin(a)}px`;
        });
        requestAnimationFrame(moveFish);
    }
    moveFish();
});
