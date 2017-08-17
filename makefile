
deploy:
	source ~/nikola/bin/activate;nikola clean;nikola build;\
	git add -A; \
    git commit -m 'update or add new post'; \
    git push origin



