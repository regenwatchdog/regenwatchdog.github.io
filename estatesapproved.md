---
layout: default
---
<div class="col">
              <ul class="row list-unstyled justify-content-center">
{% for scheme in site.data.approvedschemes %}
                <li class="col-5" data-aos="fade-up">
                  <div class="card card-sm">
                    <a href="landing-1.html">
                      <img class="card-img-top" src="{{ scheme.image_path }}" alt="Landing - One">
                    </a>
                    <div class="card-footer d-flex justify-content-between">
                      <a href="landing-1.html" class="h6 m-0">{{ scheme.name }}</a>
                      <a target="_blank" href="landing-1.html" data-toggle="tooltip" data-placement="top" title="Open in new tab"><i class="icon-popup"></i></a>
                    </div>
                  </div>
                </li>
{% endfor %}
              </ul>
</div>
