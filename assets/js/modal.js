document.addEventListener("DOMContentLoaded", function() {
  var modal = document.getElementById('desc-modal');
  var modalImg = document.getElementById('modal-img');
  var modalTitle = document.getElementById('modal-title');
  var modalAuthors = document.getElementById('modal-authors');
  var modalVenue = document.getElementById('modal-venue');
  var modalText = document.getElementById('modal-text');
  var modalEqual = document.getElementById('modal-equal');
  var modalPills = document.getElementById('modal-pills');
  var closeBtn = modal.querySelector('.modal-close');

  var figures = document.querySelectorAll('.figure-with-text');
  for (var i = 0; i < figures.length; i++) {
    (function(el) {
      var img = el.querySelector('img');
      var text = el.querySelector('.figure-text');
      if (!img || !text) return;
      img.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var card = el.closest('.project-card');
        modalImg.src = img.src;
        modalImg.alt = img.alt || '';
        modalText.innerHTML = text.innerHTML;
        var h3 = card ? card.querySelector('h3') : null;
        modalTitle.textContent = h3 ? h3.textContent : '';
        var authors = card ? card.querySelector('.authors') : null;
        modalAuthors.innerHTML = authors ? authors.innerHTML : '';
        var venue = card ? card.querySelector('.venue') : null;
        modalVenue.innerHTML = venue ? venue.innerHTML : '';
        modalVenue.style.display = venue ? '' : 'none';
        var hasEqual = authors && authors.innerHTML.indexOf('sup') !== -1;
        modalEqual.style.display = hasEqual ? '' : 'none';
        var links = card ? card.querySelector('.links.pill-links') : null;
        modalPills.innerHTML = links ? links.innerHTML : '';
        modalPills.style.display = links ? '' : 'none';
        modal.classList.add('active');
      });
    })(figures[i]);
  }

  closeBtn.addEventListener('click', function() { modal.classList.remove('active'); });
  modal.addEventListener('click', function(e) {
    if (e.target === modal) modal.classList.remove('active');
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') modal.classList.remove('active');
  });
});
