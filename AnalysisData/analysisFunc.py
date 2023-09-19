from AnalysisData import analysisBasic


def LineChart(name,LabelArr,Data,text):
    HTML="""
    <canvas id="{name}" width="400" height="200"></canvas>
<script>
const {name}_ctx = document.getElementById('{name}');
const {name}_labels = {LabelArr}
const {name}_data = {{labels: {name}_labels,
  datasets: [{{
    label: '{text}',
    data: {Data},
    fill: false,
    borderColor: 'rgb(75, 192, 192)', 
    tension: 0.1
  }}]
}};
const {name}_config = {{
  type: 'line', 
  data: {name}_data,
}};
const {name}_Chart = new Chart({name}_ctx, {name}_config);
</script>
""".format(name=name,LabelArr=LabelArr,Data=Data,text=text)
    print(HTML)
    return HTML
def BarChart(name,LabelArr,Data,text):
    HTML="""
    <canvas id="{name}" width="400" height="200"></canvas>
<script>
const {name}_ctx = document.getElementById('{name}');
const {name}_labels = {LabelArr}
const {name}_data = {{
  labels: {name}_labels,
  datasets: [{{
    label: '{text}',
    data: {Data},
    backgroundColor: [      // 设置每个柱形图的背景颜色
      'rgba(255, 99, 132, 0.2)',
      
    ],
    borderColor: [     //设置每个柱形图边框线条颜色
      
    ],
    borderWidth: 1     // 设置线条宽度
  }}]
}};
const {name}_config = {{
  type: 'bar', 
  data: {name}_data,  
  options: {{
    scales: {{
      y: {{
        beginAtZero: true 
      }}
    }}
  }},
}};
const {name}_Chart = new Chart({name}_ctx, {name}_config);
</script>
""".format(name=name,text=text,LabelArr=LabelArr,Data=Data)
    return HTML

