import fs from 'fs'
import https from 'https'
import moment from 'moment'


function convertDatasource1ToMyData(lines){
  const head = CSVtoArray(lines[0])
  console.log('head', head)
  const linesReal = lines.slice(1, lines.length - 1)
  console.log('has real line:', linesReal.length)
  console.log('line 0:', linesReal[0])
  console.log('line last:', linesReal[linesReal.length -1])

  const places = {}
  linesReal.forEach(line => {
    if(line.trim() === ''){
      console.log('cancel empty line')
    }
    const elements = CSVtoArray(line)
    if(!elements || elements.length !== head.length){
      //throw Error( `bad line:'${line}'`)
     //   console.error('bad line:', line)
      return
    }
    const place = elements[1] + (elements[0]? ('|' + elements[0]) : '')
    if(places[place]){
      //
    }else{
      const a = {
        confirmedCount : {
        },
        Lat: elements[2],
        Long: elements[3],
        source: 1,
      }
      for(let i = 4; i < head.length; i++ ){
        //a date
        const date = head[i]
        if(!/\d+\/\d+\//.test(date)){
          throw Error('the head is not a date:', date)
        }
        const dateFormated = moment(date, 'M/D/YY').format('YYYYMMDD')
        const cases = elements[i]
        if(!/\d+/.test(cases)){
          throw Error('the cases is not a number:', cases)
        }
        const casesNumbered = parseInt(cases)
        if(casesNumbered > 0){
          a.confirmedCount[dateFormated] = casesNumbered
        }
      }
      places[place] = a
    }
  })
  console.log('country sample:', Object.keys(places).slice(0, 5))
  console.log('country count:', Object.keys(places).length)
  console.log('Afghanistan:', places['Afghanistan'])
  return places

}

function mergeDeathToDatasource1(places, lines){
  const head = CSVtoArray(lines[0])
  console.log('head', head)
  const linesReal = lines.slice(1, lines.length - 1)
  console.log('has real line:', linesReal.length)
  console.log('line 0:', linesReal[0])
  console.log('line last:', linesReal[linesReal.length -1])

  linesReal.forEach(line => {
    if(line.trim() === ''){
      console.log('cancel empty line')
    }
    const elements = CSVtoArray(line)
    if(!elements || elements.length !== head.length){
      //throw Error( `bad line:'${line}'`)
      console.error('bad line:', line)
      return
    }
    const place = elements[1] + (elements[0]? ('|' + elements[0]) : '')
    if(!places[place]){
      //
    }else{
      const deadCount = {
      }
      for(let i = 4; i < head.length; i++ ){
        //a date
        const date = head[i]
        if(!/\d+\/\d+\//.test(date)){
          throw Error('the head is not a date:', date)
        }
        const dateFormated = moment(date, 'M/D/YY').format('YYYYMMDD')
        const cases = elements[i]
        if(!/\d+/.test(cases)){
          throw Error('the cases is not a number:', cases)
        }
        const casesNumbered = parseInt(cases)
        if(casesNumbered > 0){
          deadCount[dateFormated] = casesNumbered
        }
      }
      places[place].deadCount = deadCount
    }
  })
  console.log('country sample:', Object.keys(places).slice(0, 5))
  console.log('country count:', Object.keys(places).length)
  console.log('Afghanistan:', places['Afghanistan'])
  return places
}

function mergeCuredToDatasource1(places, lines){
  const head = CSVtoArray(lines[0])
  console.log('head', head)
  const linesReal = lines.slice(1, lines.length - 1)
  console.log('has real line:', linesReal.length)
  console.log('line 0:', linesReal[0])
  console.log('line last:', linesReal[linesReal.length -1])

  linesReal.forEach(line => {
    if(line.trim() === ''){
      console.log('cancel empty line')
    }
    const elements = CSVtoArray(line)
    if(!elements || elements.length !== head.length){
      //throw Error( `bad line:'${line}'`)
      console.error('bad line:', line)
      return
    }
    const place = elements[1] + (elements[0]? ('|' + elements[0]) : '')
    if(!places[place]){
      //
    }else{
      const curedCount = {
      }
      for(let i = 4; i < head.length; i++ ){
        //a date
        const date = head[i]
        if(!/\d+\/\d+\//.test(date)){
          throw Error('the head is not a date:', date)
        }
        const dateFormated = moment(date, 'M/D/YY').format('YYYYMMDD')
        const cases = elements[i]
        if(!/\d+/.test(cases)){
          throw Error('the cases is not a number:', cases)
        }
        const casesNumbered = parseInt(cases)
        if(casesNumbered > 0){
          curedCount[dateFormated] = casesNumbered
        }
      }
      places[place].curedCount = curedCount
    }
  })
  console.log('country sample:', Object.keys(places).slice(0, 5))
  console.log('country count:', Object.keys(places).length)
  console.error('Afghanistan:', places['Afghanistan'])
  return places
}

function convertDatasource1USToMyData(lines){
  const head = CSVtoArray(lines[0])
  console.log('head', head)
  const linesReal = lines.slice(1, lines.length - 1)
  console.log('has real line:', linesReal.length)
  console.log('line 0:', linesReal[0])
  console.log('line last:', linesReal[linesReal.length -1])

  const places = {}
  linesReal.forEach(line => {
    if(line.trim() === ''){
      console.log('cancel empty line')
    }
    const elements = CSVtoArray(line)
    if(!elements || elements.length !== head.length){
      //throw Error( `bad line:'${line}'`)
      console.error('bad line:', line)
      return
    }
    const placeOriginal = elements[10]
    if(!/.*, ?US$/.test(placeOriginal)){
    try{
      //throw Error(`bad line, wrong location:`)
      console.error('bad line:',placeOriginal)
      }
      catch(err){
      }
    }
    const place = 'United States of America|' + elements[10].split(',').slice(0, -1).reverse().map(e => e.trim()).join('|')
    if(places[place]){
      //
    }else{
      const a = {
        confirmedCount : {
        },
        Lat: elements[8],
        Long: elements[9],
        source: 1,
      }
      for(let i = 11; i < head.length; i++ ){
        //a date
        const date = head[i]
        if(!/\d+\/\d+\//.test(date)){
          throw Error('the head is not a date:', date)
        }
        const dateFormated = moment(date, 'M/D/YY').format('YYYYMMDD')
        const cases = elements[i]
        if(!/\d+/.test(cases)){
          throw Error('the cases is not a number:', cases)
        }
        const casesNumbered = parseInt(cases)
        if(casesNumbered > 0){
          a.confirmedCount[dateFormated] = casesNumbered
        }
      }
      places[place] = a
    }
  })
  console.log('country sample:', Object.keys(places).slice(0, 5))
  console.log('country count:', Object.keys(places).length)
  return places
}

function mergeDeathToDatasource1US(places, lines){
  const head = CSVtoArray(lines[0])
  console.log('head', head)
  const linesReal = lines.slice(1, lines.length - 1)
  console.log('has real line:', linesReal.length)
  console.log('line 0:', linesReal[0])
  console.log('line last:', linesReal[linesReal.length -1])

  linesReal.forEach(line => {
    if(line.trim() === ''){
      console.log('cancel empty line')
    }
    const elements = CSVtoArray(line)
    if(!elements || elements.length !== head.length){
      //throw Error( `bad line:'${line}'`)
      console.error('bad line:', line)
      return
    }
    const placeOriginal = elements[10]
    if(!/.*, ?US$/.test(placeOriginal)){
      throw Error(`bad line, wrong location:${placeOriginal}`)
    }
    const place = 'United States of America|' + elements[10].split(',').slice(0, -1).reverse().map(e => e.trim()).join('|')
    if(!places[place]){
      //
    }else{
      const deadCount = {
      }
      for(let i = 12; i < head.length; i++ ){
        //a date
        const date = head[i]
        if(!/\d+\/\d+\//.test(date)){
          throw Error('the head is not a date:', date)
        }
        const dateFormated = moment(date, 'M/D/YY').format('YYYYMMDD')
        const cases = elements[i]
        if(!/\d+/.test(cases)){
          throw Error('the cases is not a number:', cases)
        }
        const casesNumbered = parseInt(cases)
        if(casesNumbered > 0){
          deadCount[dateFormated] = casesNumbered
        }
      }
      places[place].deadCount = deadCount
    }
  })
  console.log('country sample:', Object.keys(places).slice(0, 5))
  console.log('country count:', Object.keys(places).length)
  console.error('United States of America|Guam:', places['United States of America|Guam'])
  return places
}

function convertDatasource2ToMyData(json){
  function confirmedCountConvert(confirmedCount){
    //convert the timestamp
    const confirmedCountNew = {}
    Object.keys(confirmedCount).forEach(date => {
      confirmedCountNew[moment(date).format('YYYYMMDD')] = 
        confirmedCount[date]
    })
    return confirmedCountNew
  }
  console.log('countries count:', Object.keys(json).length)
  //{
  //  China|Beijing : {
  //    confirmedCount : {
  //      20200101: 1,
  //      20200102: 2,
  //      ...
  //    }
  //  }
  //  ...
  //}
  const places = {}
  //ignore Global
  delete json['全球']
  Object.values(json).forEach(country => {
    const countryName = country.ENGLISH
    if(!countryName){
      console.warn('haven\'t english name:', country)
      return
    }
    const confirmedCount = country.confirmedCount
    if(!confirmedCount){
      console.warn('haven\'t confirmedCount:', country)
      return
    }
    places[countryName] = {
      confirmedCount: confirmedCountConvert(confirmedCount),
      deadCount: confirmedCountConvert(country.deadCount),
      curedCount: confirmedCountConvert(country.curedCount),
      source: 2,
    }

    //adm 1
    Object.keys(country).filter(e => e !== 'ENGLISH' &&
      e !== 'confirmedCount' &&
      e !== 'curedCount' &&
      e !== 'deadCount'
    ).forEach(key => {
      const adm1Place = country[key]
      const adm1Name = adm1Place.ENGLISH
      if(!adm1Name){
        console.warn('haven\'t english name:', adm1Place)
        return
      }
      const confirmedCount = adm1Place.confirmedCount
      if(!confirmedCount){
        console.warn('haven\'t confirmedCount:', adm1Place)
        return
      }
      places[countryName + "|" + adm1Name] = {
        confirmedCount: confirmedCountConvert(confirmedCount),
        deadCount: confirmedCountConvert(adm1Place.deadCount),
        curedCount: confirmedCountConvert(adm1Place.curedCount),
        source: 2,
      }

      //adm 2
      Object.keys(adm1Place).filter(e => e !== 'ENGLISH' &&
        e !== 'confirmedCount' &&
        e !== 'curedCount' &&
        e !== 'deadCount'
      ).forEach(key => {
        const adm2Place = adm1Place[key]
        const adm2Name = adm2Place.ENGLISH
        if(!adm2Name){
          console.warn('haven\'t english name:', adm2Name)
          return
        }
        const confirmedCount = adm2Place.confirmedCount
        if(!confirmedCount){
          console.warn('haven\'t confirmedCount:', adm2Place)
          return
        }
        places[countryName + "|" + adm1Name + "|" + adm2Name] = {
          confirmedCount: confirmedCountConvert(confirmedCount),
          deadCount: confirmedCountConvert(adm2Place.deadCount),
          curedCount: confirmedCountConvert(adm2Place.curedCount),
          source: 2,
        }

        //adm 3
        Object.keys(adm2Place).filter(e => e !== 'ENGLISH' &&
          e !== 'confirmedCount' &&
          e !== 'curedCount' &&
          e !== 'deadCount'
        ).forEach(key => {
          const adm3Place = adm2Place[key]
          const adm3Name = adm3Place.ENGLISH
          if(!adm3Name){
            console.warn('haven\'t english name:', adm3Name)
            return
          }
          const confirmedCount = adm3Place.confirmedCount
          if(!confirmedCount){
            console.warn('haven\'t confirmedCount:', adm3Place)
            return
          }
          places[countryName + "|" + adm1Name + "|" + adm2Name + "|" + adm3Name] = {
            confirmedCount: confirmedCountConvert(confirmedCount),
            deadCount: confirmedCountConvert(adm3Place.deadCount),
            curedCount: confirmedCountConvert(adm3Place.curedCount),
            source: 2,
          }

          //adm 4
          Object.keys(adm3Place).filter(e => e !== 'ENGLISH' &&
            e !== 'confirmedCount' &&
            e !== 'curedCount' &&
            e !== 'deadCount'
          ).forEach(key => {
            const adm4Place = adm3Place[key]
            const adm4Name = adm4Place.ENGLISH
            if(!adm4Name){
              console.warn('haven\'t english name:', adm4Name)
              return
            }
            const confirmedCount = adm4Place.confirmedCount
            if(!confirmedCount){
              console.warn('haven\'t confirmedCount:', adm4Place)
              return
            }
            places[countryName + "|" + adm1Name + "|" + adm2Name + "|" + adm3Name + "|" + adm4Name] = {
              confirmedCount: confirmedCountConvert(confirmedCount),
              deadCount: confirmedCountConvert(adm4Place.deadCount),
              curedCount: confirmedCountConvert(adm4Place.curedCount),
              source: 2,
            }
          })
        })
      })

    })
  })
  console.log('plases sample:', Object.keys(places).slice(0, 2))
  console.log('plases sample:', Object.keys(places).slice(0, 2))
  console.log('Afghanistan sample:', places['Afghanistan'])

  return places

}

function outputTable(places){
  //generate the output table
  const outputHead = [
    'num',
    'lat',
    'lon',
    'cases',
    'deaths',
    'recovered',
    'DayStart',
    'DayEnd',
    'placetype',
    'adm0',
    'adm1',
    'adm3',
    'adm4',
    'indiv',
    'source',
  ]
  let num = 1
  const outputLines = []
  Object.keys(places).sort((a,b) => a >= b? 1: -1).forEach(place => {

    const placeValue = places[place]
    console.log(placeValue)
    let casesAccumulated = 0
    let deadAccumulated = 0
    let curedAccumulated = 0
    Object.keys(placeValue.confirmedCount).forEach(dateString => {
      const adms = place.split('|')
      let line = ''
      const cases = parseInt(placeValue.confirmedCount[dateString])
      const dead = parseInt((placeValue.deadCount && placeValue.deadCount[dateString]) || 0)
      const cured = parseInt((placeValue.curedCount && placeValue.curedCount[dateString]) || 0)
      if(casesAccumulated === cases && 
        deadAccumulated === dead &&
        curedAccumulated === cured
      ){
        //equal cases, combine
        outputLines[outputLines.length - 1 ] = [...outputLines[outputLines.length - 1]]
        outputLines[outputLines.length - 1][7] = dateString
      }else{
        const line = [
          num++,
          placeValue.Lat? placeValue.Lat:'',
          placeValue.Long? placeValue.Long:'',
          cases,
          dead > 0?dead:'',
          cured > 0?cured:'',
          dateString,
          dateString,
          `adm${adms.length - 1}`,
          adms[0],
          adms[1]?adms[1]:'',
          adms[2]?adms[2]:'',
          adms[3]?adms[3]:'',
          '',
          placeValue.source? placeValue.source:'',
        ]
        outputLines.push(line)
        casesAccumulated = cases
        deadAccumulated = dead
        curedAccumulated = cured
      }
    })
  })
  console.log('output lines sample:', outputLines.slice(0, 20))
  console.log('output lines num:', outputLines.length)
  const countries = {
  }
  Object.keys(places).forEach(place => {
    const placeValue = places[place]
    const name = place.split('|')[0]
    const dates = Object.values(placeValue.confirmedCount)
    if(countries[name]){
      countries[name] = countries[name] + dates[dates.length - 1]
    }else{
      countries[name] = dates[dates.length - 1]
    }
  })
  console.log('countries count:', Object.keys(countries).length)
  console.log('countries sample:', Object.keys(countries).slice(0, 5))
  console.log('countries cases sample:', Object.values(countries).slice(0, 5))
  return {
    outputLines: [outputHead, ...outputLines],
    places,
    countries
  }
}

function outputTableLocation(places){
  //generate the output table
  const outputHead = [
    'num',
    'placetype',
    'adm0',
    'adm1',
    'adm3',
    'adm4',
    'indiv',
  ]
  let num = 1
  const outputLines = []
  Object.keys(places).sort((a,b) => a >= b? 1: -1).forEach(place => {
    const adms = place.split('|')
    const line = [
      num++,
      `adm${adms.length - 1}`,
      adms[0],
      adms[1]?adms[1]:'',
      adms[2]?adms[2]:'',
      adms[3]?adms[3]:'',
    ]
    outputLines.push(line)
  })
  console.log('output lines sample:', outputLines.slice(0, 20))
  console.log('output lines num:', outputLines.length)
  return {
    outputLines: [outputHead, ...outputLines],
    places,
  }
}

function run(){
  //data source 1
  let places1 = {}
  let places1US = {}
  let places2 = {}
  fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv').then(data => {
    console.log('DS1, confirm...')
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    places1 = convertDatasource1ToMyData(lines)
  }).then(() => {
    return fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
  }).then(data => {
    console.log('DS1, death...')
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    mergeDeathToDatasource1(places1, lines)
  }).then(() => {
    return fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
  }).then(data => {
    console.log('DS1, recover...')
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    mergeCuredToDatasource1(places1, lines)
  }).then(data => {
    return fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
  }).then(data => {
    console.log('DS1US, confirm...')
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    places1US = convertDatasource1USToMyData(lines)
  }).then(() => {
    return fetch('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
  }).then(data => {
    console.log('DS1US, death...')
    const dataString = data.toString()
    console.log('sample data:', dataString.slice(0, 200))
    const lines = dataString.split(/\n/)
    console.log('has line:', lines.length)
    console.log('line 0:', lines[0])
    console.log('line last:', lines[lines.length -1])
    mergeDeathToDatasource1US(places1US, lines)
  }).then(() => {
    return fetch('https://raw.githubusercontent.com/nittyjee/coronastate/master/data/newjob/all.json')
  }).then(data => {
    console.log('DS2...')
    const json = JSON.parse(data.toString())
    places2 = convertDatasource2ToMyData(json)
  }).then(() => {

    //all table
    {
      //merge
      let places = {}
      Object.assign(places, places2, places1US, places1)
      const result = outputTable(places)
      //output
      fs.writeFileSync(
        '../data/all.csv',
        result.outputLines.reduce((a,c,i) => {
          {return i === 0 ? c: (a + '\n' + c)}
        },'')
      )
      fs.writeFileSync(
        '../data/report.csv',
        'total area, total countries,last update' + '\n' + 
        Object.keys(result.places).length + ',' + 
        Object.keys(result.countries).length + ',' + 
        '"' + new Date().toUTCString() + '"' + 
        '\n'
      )
      //locations table
      {
        const result = outputTableLocation(places)
        fs.writeFileSync(
          '../data/locations.csv',
          result.outputLines.reduce((a,c,i) => {
            {return i === 0 ? c: (a + '\n' + c)}
          },'')
        )
      }
    }

    //datasource 1 table
    {
      //merge
      let places = {}
      Object.assign(places, places1US, places1)
      const result = outputTable(places)
      //output
      fs.writeFileSync(
        '../data/datasource1.csv',
        result.outputLines.reduce((a,c,i) => {
          {return i === 0 ? c: (a + '\n' + c)}
        },'')
      )
    }
    {
      //merge
      let places = {}
      Object.assign(places, places2)
      const result = outputTable(places)
      //output
      fs.writeFileSync(
        '../data/datasource2.csv',
        result.outputLines.reduce((a,c,i) => {
          {return i === 0 ? c: (a + '\n' + c)}
        },'')
      )
    }
  })
}


function fetch(url){
  return new Promise((resolve, reject) => {
    https.get(url, (resp) => {
      let data = '';
      // A chunk of data has been recieved.
      resp.on('data', (chunk) => {
        data += chunk;
      });
      // The whole response has been received. Print out the result.
      resp.on('end', () => {
        console.log('fetch data sameple:', data.slice(0,100));
        resolve(data)
      });
    }).on("error", (err) => {
      console.log("Error: " + err.message);
    });
  })
}

// Return array of string values, or NULL if CSV string not well formed.
function CSVtoArray(text) {
    var re_valid = /^\s*(?:'[^'\\]*(?:\\[\S\s][^'\\]*)*'|"[^"\\]*(?:\\[\S\s][^"\\]*)*"|[^,'"\s\\]*(?:\s+[^,'"\s\\]+)*)\s*(?:,\s*(?:'[^'\\]*(?:\\[\S\s][^'\\]*)*'|"[^"\\]*(?:\\[\S\s][^"\\]*)*"|[^,'"\s\\]*(?:\s+[^,'"\s\\]+)*)\s*)*$/;
    var re_value = /(?!\s*$)\s*(?:'([^'\\]*(?:\\[\S\s][^'\\]*)*)'|"([^"\\]*(?:\\[\S\s][^"\\]*)*)"|([^,'"\s\\]*(?:\s+[^,'"\s\\]+)*))\s*(?:,|$)/g;
    // Return NULL if input string is not well formed CSV string.
    if (!re_valid.test(text)) return null;
    var a = [];                     // Initialize array to receive values.
    text.replace(re_value, // "Walk" the string using replace with callback.
        function(m0, m1, m2, m3) {
            // Remove backslash from \' in single quoted values.
            if      (m1 !== undefined) a.push(m1.replace(/\\'/g, "'"));
            // Remove backslash from \" in double quoted values.
            else if (m2 !== undefined) a.push(m2.replace(/\\"/g, '"'));
            else if (m3 !== undefined) a.push(m3);
            return ''; // Return empty string.
        });
    // Handle special case of empty last value.
    if (/,\s*$/.test(text)) a.push('');
    return a;
}

export {
  fetch, 
  CSVtoArray, 
  run, 
  convertDatasource1ToMyData,
  convertDatasource1USToMyData, 
  convertDatasource2ToMyData, 
  outputTable,
  outputTableLocation,
  mergeDeathToDatasource1,
  mergeCuredToDatasource1,
  mergeDeathToDatasource1US,
}

