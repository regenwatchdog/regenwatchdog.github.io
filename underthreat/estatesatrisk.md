---
layout: default
title: estates under threat
category: underthreat
---
<div class="col">
<iframe src="/leafletmap.html" width="100%" height="400px"></iframe>
<p align="right">Click <a href="/leafletmap.html">here</a> to open map in new window.</p>
</div>
   

<div class="col">
              <ul class="row list-unstyled justify-content-center">
{% for estate in site.estates %}
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
{% endfor %}
              </ul>
</div>

