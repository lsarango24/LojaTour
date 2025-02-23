if ( !mobilecheck() ) {
	$(".player").mb_YTPlayer({
		onReady: function(){
			jQuery('.sound').show();
			jQuery('.sound').click(function(evt){
				evt.preventDefault();
			  	if(jQuery('.sound').hasClass('off')){
				    jQuery('.sound').removeClass('off');
				    jQuery('.player').unmuteYTPVolume();
				    jQuery('.sound').addClass('on');
				    jQuery('.title').fadeOut();
				    jQuery('.travelogue-icon-sound').removeClass('fa-volume-off');
					jQuery('.travelogue-icon-sound').addClass('fa-volume-up');
			   	}else{
				    if(jQuery('.sound').hasClass('on')){
				        jQuery('.sound').removeClass('on');
				        jQuery('.player').muteYTPVolume();    
				        jQuery('.sound').addClass('off');
				        jQuery('.title').fadeIn();
				        jQuery('.travelogue-icon-sound').removeClass('fa-volume-up');
						jQuery('.travelogue-icon-sound').addClass('fa-volume-off');
				    }
				}           
			});
		}
	});
	$('.player').on("YTPStart",function(){
	   $('.video-bg').animate({opacity: 1}, 5000,function(){});
	});
}
