from django.shortcuts import render
# from bokeh.plotting import figure as bfigure
# from bokeh.resources import CDN as bcdn
# from bokeh.embed import components as bcomponents
import bokeh

# Create your views here.
print ("vc")

def display_graph(request):
    plot = bfigure()
    plot.circle([1,2], [3,4])

    print ("dg")
    script, div = bcomponents(plot, bcdn)

    return render(request, "consumption_client.html", {"the_script": script, "the_div": div})

