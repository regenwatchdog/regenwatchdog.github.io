---
layout: default
title: Estates under threat in Havering 
category: underthreat
---

<div class="col">
              <ul class="row list-unstyled justify-content-center">
{% assign schemes = site.estates | where:"borough","havering" %}
  {% for scheme in schemes %}
                <li class="col-5" data-aos="fade-up">
                  <div class="card card-sm">
                    <a href="{{ scheme.url }}">
                      <img class="card-img-top" src="{{ scheme.images.first.image_path }}" alt="{{ scheme.name }}">
                    </a>
		    <div class="card-body">
                      <h5 class="card-title">{{ scheme.name }}</h5>
		      <h6 class="card-subtitle mb-2 text-muted">{{ scheme.fullname }}</h6>
		      <p class="card-text">{{ scheme.excerpt }}</p>
                      <a target="_blank" href="{{ scheme.url }}" data-toggle="tooltip" data-placement="top" title="Open in new tab">Read more here: <i class="icon-popup"></i></a>
                  </div>
                  </div>
                </li>
{% endfor %}
              </ul>
</div>
