import fs from 'fs'
import https from 'https'
import moment from 'moment'
import {
  CSVtoArray, 
  fetch, 
  convertDatasource1ToMyData,
  convertDatasource1USToMyData, 
  convertDatasource2ToMyData, 
  outputTable,
  outputTableLocation,
  mergeDeathToDatasource1,
  mergeCuredToDatasource1,
  mergeDeathToDatasource1US,
} from './main.js'

describe('moment', () => {
  it('2/24/20 -> 20200122', () => {
    console.log(moment('2/24/20','M/D/YY').format('YYYYMMDD'))
  })

  it('UTC', () => {
    console.log(new Date().toUTCString())
  })

})

describe('test', () => {

  it('datasource1', () => {
    const data = fs.readFileSync('./samples/source1.csv') 
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    const places = convertDatasource1ToMyData(lines)
    
    //merge death
    {
      const data = fs.readFileSync('./samples/time_series_covid19_deaths_global.csv') 
      const dataString = data.toString()
      console.log('sample data:', dataString.slice(0, 200))
      const lines = dataString.split(/\n/)
      console.log('has line:', lines.length)
      console.log('line 0:', lines[0])
      console.log('line last:', lines[lines.length -1])
      mergeDeathToDatasource1(places, lines)
    }

    //merge cured
    {
      const data = fs.readFileSync('./samples/time_series_covid19_recovered_global.csv') 
      const dataString = data.toString()
      console.log('sample data:', dataString.slice(0, 200))
      const lines = dataString.split(/\n/)
      console.log('has line:', lines.length)
      console.log('line 0:', lines[0])
      console.log('line last:', lines[lines.length -1])
      mergeCuredToDatasource1(places, lines)
    }

    outputTable(places)
  })

  it('datasource1-us', () => {
    const data = fs.readFileSync('./samples/time_series_covid19_confirmed_US.csv') 
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    const places = convertDatasource1USToMyData(lines)

    //merge death
    {
      const data = fs.readFileSync('./samples/time_series_covid19_deaths_US.csv') 
      const dataString = data.toString()
      console.log('sample data:', dataString.slice(0, 200))
      const lines = dataString.split(/\n/)
      console.log('has line:', lines.length)
      console.log('line 0:', lines[0])
      console.log('line last:', lines[lines.length -1])
      mergeDeathToDatasource1US(places, lines)
    }

    outputTable(places)
  })

  it('datasource2', () => {
    const data = fs.readFileSync('./samples/source2.json')
    const json = JSON.parse(data.toString())
    const places = convertDatasource2ToMyData(json)
    const result = outputTable(places)
    console.log('output table sample:', result.outputLines.slice(0, 5))
  })

  it('print location table', () => {
    const data = fs.readFileSync('./samples/source2.json')
    const json = JSON.parse(data.toString())
    const places = convertDatasource2ToMyData(json)
    const result = outputTableLocation(places)
    console.log('output table sample:', result.outputLines.slice(0, 5))
  })


  it.skip('fetch data from url datasource 1 global ', () => {
    return fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
  })

  it.skip('fetch data from url datasource 1 us ', () => {
    return fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
  })

  it.skip('fetch data from url datasource 2', () => {
    return fetch('https://raw.githubusercontent.com/stevenliuyi/covid19/master/public/data/all.json')
  }, 100000)

  it('split csv line', () => {
    const line = '316,GU,GUM,316,66.0,,Guam,US,13.4443,144.7937,"Guam, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,5,12,14,15,27,29,32,37,45,51,55,56,58,69,77,82,84,93,112,113,121,121,128,130,133,133,133'
    console.log(CSVtoArray(line))
  })
})
