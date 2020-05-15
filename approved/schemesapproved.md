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
Estate regeneration usually starts off with worthy intentons like plentiful replacement affordable housing and generous offers to residents, but evidence shows that an increasing number of schemes fail to comply even with the basic policy requirements. The Mayor's <a href="http://estatewatch.london/guide/#headingOne">estate regeneration policy</a> says that schemes must provide:
<ul>
		      <li>At least 50% affordable and no net loss of social rent.</li>
		      <li>A fair deal and right to return for residents.</li>
		      <li>That demolition is considered only as last resort</li>
                </ul>
</p>
<p class="lead text-muted" align="left">
Despite this the Mayor has signed off at least xx schemes that fail to comply with these requirements and continues to turn a blind eye to Councils, housing associations and developers flouting these rules. </p>
				
				 
	     </div>
 </section>












              <ul class="row list-unstyled justify-content-center">
{% for scheme in site.data.approvedschemes %}
                <li class="col-5" data-aos="fade-up">
                  <div class="card card-sm">
                    <a href="{{ scheme.url }}">
                      <img class="card-img-top" src="{{ scheme.image_path }}" alt="{{ scheme.name }}">
                    </a>
		    <div class="card-body">
                      <h5 class="card-title">{{ scheme.name }}</h5>
		      <h6 class="card-subtitle mb-2 text-muted">{{ scheme.fullname }}</h6>
		      <p class="card-text">{{ scheme.comment }}</p>
                      <a target="_blank" href="{{ scheme.url }}" data-toggle="tooltip" data-placement="top" title="Open in new tab">Approved: {{ scheme.date }} <i class="icon-popup"></i></a>
                  </div>
                  </div>
                </li>
{% endfor %}
              </ul>
</div>

