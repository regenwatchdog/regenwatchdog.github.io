---
title: Monthly News Updates 
layout: default
category: updates
---

<div class="col-12 col-md-8">
<ul class="row feature-list">
  {% for post in site.posts %}
      <li id="accordion" class="col-12">

            <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1><b>{{ post.date | date_to_string }}</b>

		          {{ post.excerpt }}

		      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
          </li>
    {% endfor %}
    </ul>
   </div>
