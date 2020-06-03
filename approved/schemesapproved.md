---
layout: default
title: What is wrong with estate regeneration?
category: approved
---

<div class="col">



    <section class="jumbotron text-center">
	     <div class="container">
		           <h1>The path to regeneration is paved with good intentions</h1>
			         <p class="lead text-muted" align="left">
Estate regeneration always starts off with worthy intentons - i.e. promises of plentiful 'affordable' housing and brand new homes for residents, but evidence shows that in reality many schemes fail to comply even with basic policy requirements. The Mayor's <a href="http://estatewatch.london/guide/#headingOne">estate regeneration policy</a> says that schemes must provide at least 50% affordable housing and that there must be no net loss of social rented housing.</p>

<p class="lead text-muted" align="left">
Despite this the Mayor has signed off at least xx schemes that fail to provide 50% affordable and have substituted replacement social rented housing for affordable rent (i.e. up to 80% market rent). </p>
				
				 
	     </div>
 </section>



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

