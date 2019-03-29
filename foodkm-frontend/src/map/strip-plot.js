import {select,selectAll} from 'd3-selection'
import {scaleLinear} from 'd3-scale'
import {extent} from 'd3-array'

export default class stripPlot {
  constructor(opts) {
    Object.assign(this, opts);

    this.makeSettings()
    this.makeScales()
    this.appendElements()
    this.render()

    window.onresize = () => {
      this.render()
    }

  }

  makeSettings() {
    this.width = select(this.element).node().offsetWidth
    this.height = 55

    this.margin = {
      'left' : 70,
      'right' : 90,
      'top' : 30,
      'bottom' : 30,
    }
  }

  makeScales() {

    this.extent = extent(this.data)

    this.xScale = scaleLinear()
      .domain(this.extent)
      .range([0, this.width-this.margin.left-this.margin.right])
  }

  appendElements() {

    this.svg = select(this.element).select('svg')

    this.g = this.svg.append('g')

    this.axis = this.g.append('g')
    this.axisLine = this.axis.append('line').attr('class','axis-line')
    this.minLabel = this.axis.append('text').attr('class','axis-overlabel').attr('text-anchor','end').text('Min')
    this.maxLabel = this.axis.append('text').attr('class','axis-overlabel').text('Max')
    this.min = this.axis.append('text').attr('class','axis-label').attr('text-anchor','end').text(this.extent[0].toFixed(1) +'km')
    this.max = this.axis.append('text').attr('class','axis-label').text(this.extent[1].toFixed(1) +'km')

    this.circles = this.g.selectAll('circle')
      .data(this.data)
      .enter()
      .append('circle')
      .attr('r', 4)
      .attr('class','circle')

  }

  render() {
    
    this.svg
      .attr('width', this.width)
      .attr('height', this.height)

    this.g.attr('transform', 'translate('+this.margin.left+','+this.margin.top+')')
    this.axisLine
      .attr('y1', 0)
      .attr('y2', 0)
      .attr('x1', 0)
      .attr('x2', this.width-this.margin.left-this.margin.right)

    this.min.attr('y', 4).attr('x', -10)
    this.max.attr('y', 4).attr('x', this.width-this.margin.left-this.margin.right+10)

    this.minLabel.attr('y', -20).attr('x', -10)
    this.maxLabel.attr('y', -20).attr('x', this.width-this.margin.left-this.margin.right+10)

    this.circles.attr('cx', d => {
      return this.xScale(d)
    })
  }


  
}
