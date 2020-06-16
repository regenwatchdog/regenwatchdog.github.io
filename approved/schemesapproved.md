---
layout: default
title: From social to unaffordable rent 
category: approved
published: true
---

<div class="col">



    <section class="jumbotron text-center">
	     <div class="container">
	           <h3>From social to 'affordable' housing</h3>
<p class="lead text-muted" align="left">
The Mayor's <a href="http://estatewatch.london/guide/#headingOne">estate regeneration policy</a> says that schemes should provide at least 50% affordable housing and that there should be no net loss of social rented housing.

Despite this the Mayor is signing off an increasing number of schemes that fail to meet these requirements and which have substituted social rented housing for affordable rent (i.e. up to 80% market rent) - here are a few examples, which we will add to over time: 
</p>
				
				 
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

