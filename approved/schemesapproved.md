---
layout: default
title: From social to unaffordable rent 
category: approved
published: false
---

<div class="col">



    <section class="jumbotron text-center">
	     <div class="container">
	           <h3>From social to 'affordable' housing</h3>
			         <p class="lead text-muted" align="left">
The theory goes that estates in high-value areas are able to re-provide the existing levels of social housing via cross-subsidy from private housing, either for sale or rent, reinforced by increased density. In practice these good intentions get <a href="https://www.theguardian.com/cities/2015/jun/25/london-developers-viability-planning-affordable-social-housing-regeneration-oliver-wainwright">squeezed</a> by developers whose bottom line is profit and housing associations who have lost government grant and now <a href="https://commonslibrary.parliament.uk/research-briefings/sn01090/">actively lobby</a> for the ability to set their own rents as part of their new <a href="https://www.theguardian.com/society/2018/jun/13/fury-affordable-homes-redeveloped-sold-housing-associations">corporate aims</a>.</p>

</div>
</section>


 <div class="container">

      <div class="row">

  

        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <img class="bd-placeholder-img card-img-top" width="100%" src="/images/guardianheygate.png" alt="The carcass" data-action="zoom" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
            <div class="card-body">
              <p class="card-text">How developers exploit the planning system.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <a href="https://www.theguardian.com/cities/2015/jun/25/london-developers-viability-planning-affordable-social-housing-regeneration-oliver-wainwright" data-action="zoom" class="btn btn-sm btn-outline-secondary">Read</a>
                </div>
              </div>
            </div>
          </div>
        </div>
 

        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <img class="bd-placeholder-img card-img-top" width="100%" src="/images/insidehousingsr.png" alt="Empty shell" data-action="zoom" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
            <div class="card-body">
              <p class="card-text">4% of new affordable housing is social rent.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <a href="https://www.insidehousing.co.uk/insight/insight/the-social-rent-dilemma-64425" data-action="zoom" class="btn btn-sm btn-outline-secondary">Read</a>
                </div>
              </div>
            </div>
          </div>
        </div>
 

        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
            <img class="bd-placeholder-img card-img-top" width="100%" src="/images/hocrentsetting.png" alt="The frame" data-action="zoom" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
            <div class="card-body">
              <p class="card-text">Housing associations <a href="https://commonslibrary.parliament.uk/research-briefings/sn01090/lobby">lobby</a> for <a href="NHFRentFreedom2017.pdf">rent freedom.</a></p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <a href="https://commonslibrary.parliament.uk/research-briefings/sn01090/" data-action="zoom" class="btn btn-sm btn-outline-secondary">Read</a>
                </div>
              </div>
            </div>
          </div>
        </div>
 

<p class="lead text-muted" align="left">
The Mayor's <a href="http://estatewatch.london/guide/#headingOne">estate regeneration policy</a> says that schemes should provide at least 50% affordable housing and that there should be no net loss of social rented housing.

Despite this the Mayor is signing off an increasing number of schemes that fail to meet these requirements and which have substituted social rented housing for affordable rent (i.e. up to 80% market rent): 
</p>
				
				 
	     </div>
<br>
<br>


             <ul class="row list-unstyled justify-content-center">
{% for estate in site.estates %}
{% if estate.erg contains "noncompliant" %}
                <li class="col-5" data-aos="fade-up">
                  <div class="card card-sm">
                    <a href="{{ estate.url }}">
                      <img class="card-img-top" src="{{ estate.images.first.image_path }}" alt="{{ estate.name }}">
                    </a>
		    <div class="card-body">
                      <h5 class="card-title">{{ estate.name }}</h5>
		      <h6 class="card-subtitle mb-2 text-muted">Status: {{ estate.status }}</h6>
		      <p class="card-text">{{ estate.excerpt }}</p>
                      <a target="_blank" href="{{ estate.url }}" data-toggle="tooltip" data-placement="top" title="Open in new tab">Read more here: <i class="icon-popup"></i></a>
                  </div>
                  </div>
                </li>
{% endif %}
{% endfor %}
              </ul>
</div>

