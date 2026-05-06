from django.db import models


class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.role} — {self.company}"

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def get_period(self):
        start = self.start_date.strftime('%b %Y')
        end = 'Presente' if self.current else self.end_date.strftime('%b %Y')
        return f"{start} – {end}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('data', 'Análisis de Datos'),
        ('viz', 'Visualización'),
        ('prog', 'Programación'),
        ('db', 'Bases de Datos'),
        ('tool', 'Herramientas'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80)
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-proficiency']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    technologies = models.CharField(max_length=500, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]
