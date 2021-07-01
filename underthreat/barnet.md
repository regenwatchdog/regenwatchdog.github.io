---
layout: default
title: Barnet 
category: underthreat
---
<div class="col">
<div class="embed-responsive embed-responsive-16by9">
<iframe src="{{ site.baseurl }}/underthreat/barnetmap.html" width="100%" height="400px"></iframe>
</div>
<p align="right">Click <a href="{{ site.baseurl }}/underthreat/barnetmap.html">here</a> to open map in new window.</p>
</div>
<br>
<div class="col">
              <ul class="row list-unstyled justify-content-center">
{% assign schemes = site.estates | where:"borough","barnet" %}
  {% for scheme in schemes %}
                <li class="col-5" data-aos="fade-up">
                  <div class="card card-sm">
                    <a href="{{ scheme.url }}">
                      <img class="card-img-top" src="{{ scheme.images.first }}" alt="{{ scheme.name }}">
                    </a>
		    <div class="card-body">
		    <a href="{{ scheme.url }}">
                      <h5 class="card-title">{{ scheme.name }}</h5>
		      </a>
		      <h6 class="card-subtitle mb-2 {% if scheme.stage == 'Preparation' %}text-warning{% elsif scheme.stage == 'Implementation' %}text-danger{% elsif scheme.stage == 'Proposal' %}text-success{% endif %}">Stage: {{ scheme.stage }}</h6>
		      <p class="card-text">{{ scheme.excerpt }}</p>
                      <a target="_blank" href="{{ scheme.url }}" data-toggle="tooltip" data-placement="top" title="Open in new tab">Read more here: <i class="icon-popup"></i></a>
                  </div>
                  </div>
                </li>
{% endfor %}
              </ul>
</div>
