---
layout: default
title: schemes approved
category: approved
---

<div class="col">



    <section class="jumbotron text-center">
	     <div class="container">
		           <h1>Non-compliant schemes</h1>
			         <p class="lead text-muted" align="left">
Estate regeneration usually starts off with worthy intentons like plentiful replacement affordable housing and generous offers to residents but the evidence shows that ultimately many schemes fail to even comply the basic minimum requirements. The Mayor's estate regeneration policy says that schemes must comply with the following requirements:
<ul>
		      <li>At least 50% affordable and no net loss of social rent.</li>
		      <li>A fair deal and right to return for residents.</li>
		      <li>Demolition considered only as a last resort</li>
                </ul>
</p>
<p class="lead text-muted" align="left">
Despite this the Mayor has signed off at least xx estate regeneration schemes that fail to comply with these minimum requirements. </p>
				
				 
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

