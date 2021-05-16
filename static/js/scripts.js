<script>
  $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
  });
</script>
<script>
  $(document).ready(function(){
    $('#mycarousel').carousel({ interval: 2000});
    $('#carouselButton').click(function(){
      if($('#carouselButton').children('span').hasClass('fa-pause')){
        $('#mycarousel').carousel('pause');
        $('#carouselButton').children('span').removeClass('fa-pause');
        $('#carouselButton').children('span').addClass('fa-play');
      }
      else if($('#carouselButton').children('span').hasClass('fa-play')){
        $('#mycarousel').carousel('cycle');
        $('#carouselButton').children('span').removeClass('fa-play');
        $('#carouselButton').children('span').addClass('fa-pause');
      }
    });

  })
</script>
<script>

$(document).ready(function(){
    $('#loginModalbutton').click(function(){
      $('#loginModal').modal('show');
    });
    $('#reservetable').click(function(){
      $('#reservetableModal').modal('show');
    });
    $('#reservetableModalcross').click(function(){
      $('#reservetableModal').modal('hide');
    });
    $('#reservetableModalCancel').click(function(){
      $('#reservetableModal').modal('hide');
    });
    $('#loginModalcross').click(function(){
      $('#loginModal').modal('hide');
    });
    $('#loginModalCancel').click(function(){
      $('#loginModal').modal('hide');
    });
  });
</script>
