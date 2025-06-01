document.addEventListener('DOMContentLoaded', function() {
    // Handle video previews on hover
    const videoCards = document.querySelectorAll('.video-card');
    
    videoCards.forEach(card => {
        const previewVideo = card.querySelector('.preview-video');
        
        if (previewVideo) {
            card.addEventListener('mouseenter', () => {
                previewVideo.currentTime = 0;
                previewVideo.play().catch(e => console.log('Preview play failed:', e));
            });
            
            card.addEventListener('mouseleave', () => {
                previewVideo.pause();
            });
        }
    });
});
