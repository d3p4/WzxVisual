(function () {
    require.config({
        paths: {
			echarts: "echarts",
		},
    });

    require(
    [
        "echarts",
        "echarts/chart/main",
		"echarts/chart/map",	
    ],
    function (echarts, BMapExtension) {
        $('#main').css({
            height:$('body').height(),
            width:$('body').width()
        });

        // 初始化地图
        var BMapExt = new BMapExtension($('#main')[0], BMap, echarts,{
            enableMapClick: false
        });
        var map = BMapExt.getMap();
        var container = BMapExt.getEchartsContainer();

        var startPoint = {
            x: 121.326966, //上海南站 
            y: 31.200723
        };

        var point = new BMap.Point(startPoint.x, startPoint.y);
        map.centerAndZoom(point, 17);
        map.enableScrollWheelZoom(true);
        // 地图自定义样式
        map.setMapStyle({
           styleJson: [
          {
                    'featureType': 'land',     //调整土地颜色
                    'elementType': 'geometry',
                    'stylers': {
                              //'color': '#081734'
                              'color': '##F7F7F7'
                    }
          },
          {
                    'featureType': 'building',   //调整建筑物颜色
                    'elementType': 'geometry',
                    'stylers': {
                              //'color': '#04406F'
                              'color': '#A52A2A'
                    }
          },
         {
                    'featureType': 'building',   //调整建筑物标签是否可视
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'highway',     //调整高速道路颜色
                    'elementType': 'geometry',
                    'stylers': {
                    'color': '#015B99'
                    }
          },
          {
                    'featureType': 'highway',    //调整高速名字是否可视
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'arterial',   //调整一些干道颜色
                    'elementType': 'geometry',
                    'stylers': {
                    //'color':'#003051'
                    'color':'#4169E1'
                    }
          },
          {
                    'featureType': 'arterial',
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'green',
                    'elementType': 'geometry',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'water',
                    'elementType': 'geometry',
                    'stylers': {
                              'color': '#044161'
                    }
          },
          {
                    'featureType': 'subway',    //调整地铁颜色
                    'elementType': 'geometry.stroke',
                    'stylers': {
                    'color': '#003051'
                    }
          },
          {
                    'featureType': 'subway',
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'railway',
                    'elementType': 'geometry',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'railway',
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'all',     //调整所有的标签的边缘颜色
                    'elementType': 'labels.text.stroke',
                    'stylers': {
                              'color': '#313131'
                    }
          },
          {
                    'featureType': 'all',     //调整所有标签的填充颜色
                    'elementType': 'labels.text.fill',
                    'stylers': {
                              'color': '#FFFFFF'
                    }
          },
          {
                    'featureType': 'manmade',   
                    'elementType': 'geometry',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'manmade',
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'local',
                    'elementType': 'geometry',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'local',
                    'elementType': 'labels',
                    'stylers': {
                    'visibility': 'off'
                    }
          },
          {
                    'featureType': 'subway',
                    'elementType': 'geometry',
                    'stylers': {
                              'lightness': -65
                    }
          },
          {
                    'featureType': 'railway',
                    'elementType': 'all',
                    'stylers': {
                              'lightness': -40
                    }
          },
          {
                    'featureType': 'boundary',
                    'elementType': 'geometry',
                    'stylers': {
                              'color': '#8b8787',
                              'weight': '1',
                              'lightness': -29
                    }
          }
    ]
        });

option = {
	
    color: ['gold','aqua','lime'],
    title : {
        text: '',
        subtext: '',
        x:'center',
        textStyle : {
            color: '#fff',
			fontSize:20,
			fontWeight:'bold',
        }
    },
    tooltip : {
        show: true,
		trigger:'item',
		hideDelay:4000,
        formatter: function(d) {
			var jw= '经度：'+d.value[0]+'<br/>'
			    jw += '纬度：'+d.value[1]
			return jw       
        }
	},
	color:['gold','red'],
	legend:{
		data:['正常轨迹','调整轨迹'],
		x:'left',
		orient:'vertical',
		padding:[30,15,15,30],
		textStyle:{
			fontSize:17,
			color:'rgb(204,204,204)',
		},
		selected:{
			'正常轨迹':true,
			'调整轨迹':false,
		},
		selectedMode:'single',
	},
	/*
    toolbox: {
        show : true,
        orient : 'vertical',
        x: 'right',
        y: 'center',
        feature : {
           mark : {show: true},
           dataView : {show: true, readOnly: false},
           restore : {show: true},
           saveAsImage : {show: true}
        }
    },*/
  series : [
{
	  name:'正常轨迹',
      type:'map',
      mapType: 'none',
      data:[],
      
      markLine : {
      Symbol:['none', 'arrow'],
      symbolSize:['0', '0.1'],
      smooth:true,
      smooth:0,
      effect : {
          show: true,
          scaleSize: 1,
          period: 30,
          color: '#fff',
          shadowBlur: 10
      },
      itemStyle : {
          color: 'red',
          normal: {
              color:function(param){
              return(param.data[0].value.colorValue);
              },
              borderWidth:3,
              lineStyle: {
                  type: 'solid',
                  width: 3,
                  shadowBlur: 10
              },
              label:{show:false,value:'上海南站'}
        }
      },

    data : [
	            [{name:'p1'}, {name:'p2',value:{colorValue:'gold'}}],
                [{name:'p2'}, {name:'p3',value:{colorValue:'gold'}}],
                [{name:'p3'}, {name:'p4',value:{colorValue:'gold'}}],
				[{name:'p4'}, {name:'p5',value:{colorValue:'gold'}}],
				[{name:'p5'}, {name:'p6',value:{colorValue:'gold'}}],
				[{name:'p6'}, {name:'p7',value:{colorValue:'gold'}}],
				[{name:'p7'}, {name:'p8',value:{colorValue:'gold'}}],
				[{name:'p8'}, {name:'p9',value:{colorValue:'gold'}}],
				[{name:'p9'}, {name:'p10',value:{colorValue:'gold'}}],
				[{name:'p10'}, {name:'p11',value:{colorValue:'gold'}}],
				[{name:'p11'}, {name:'p12',value:{colorValue:'gold'}}],
				[{name:'p12'}, {name:'p13',value:{colorValue:'gold'}}],
				[{name:'p13'}, {name:'p14',value:{colorValue:'gold'}}],
				[{name:'p14'}, {name:'p15',value:{colorValue:'gold'}}]
		]
		},
	  markPoint:{
			symbol:'image://./image/location.svg',
			symbolSize:function(v){
				return v/5
			},
			effect:{
			    show:true,
                type:'bounce',
                period:3,				
			},
			itemStyle:{
				normal:{
					label:{
						show:false,
					},
				},
				emphasis:{
					label:{
						show:false,
					},
				},
			},
			data:[
			   {name:'p1',value:50,
			       tooltip:{
					   formatter:'时间:8:30am<br/>出发地:上海虹桥'
				   },
			   },
			   {name:'p16',value:100,
			       tooltip:{
					   formatter:'上海南站<br/>经度:121.326966<br/>纬度:31.200723'  
				   },
			   },
			   {name:'p15',value:50,
			       tooltip:{
					   formatter:'时间:10:00am<br/>目的地:真光小区'
				   },
			   },
			],
		},
      geoCoord:{
                 'p1':[121.326966,31.200723],
                 'p2':[121.328966,31.220723],
                 'p3':[121.336966,31.240723],
                 'p4':[121.451855,31.251429],
                 'p5':[121.461855,31.256429],
                 'p6':[121.460855,31.257429],
                 'p7':[121.458855,31.257729],
                 'p8':[121.456855,31.257829],
                 'p9':[121.454855,31.257929],
                 'p10':[121.446394,31.259887],
                 'p11':[121.432394,31.259987],
                 'p12':[121.429394,31.260887],
                 'p13':[121.428394,31.261887],
                 'p14':[121.419394,31.263887],
                 'p15':[121.419394,31.266887],
	 'p16':[121.409394,31.269887]
    }
},
	
	
	
{
	  name:'调整轨迹',
      type:'map',
      mapType: 'none',
      data:[],
      
      markLine : {
      Symbol:['none', 'arrow'],
      symbolSize:['0', '0.1'],
      smooth:true,
      smooth:20,
      effect : {
          show: true,
          scaleSize: 1,
          period: 30,
          color: '#fff',
          shadowBlur: 10
      },
      itemStyle : {
          color: 'red',
          normal: {
              color:function(param){
              return(param.data[0].value.colorValue);
              },
              borderWidth:3,
              lineStyle: {
                  type: 'solid',
                  width: 3,
                  shadowBlur: 10
              },
              label:{show:false,value:'上海南站'}
        }
      },

    data : [
	            [{name:'s1'}, {name:'s2',value:{colorValue:'gold'}}],
                [{name:'s2'}, {name:'s3',value:{colorValue:'gold'}}],
                [{name:'s3'}, {name:'s4',value:{colorValue:'gold'}}],
				[{name:'s4'}, {name:'s10',value:{colorValue:'gold'}}],
				[{name:'s10'}, {name:'s11',value:{colorValue:'gold'}}],
				[{name:'s5'}, {name:'s6',value:{colorValue:'gold'}}],
				[{name:'s6'}, {name:'s7',value:{colorValue:'gold'}}],
				[{name:'s7'}, {name:'s8',value:{colorValue:'gold'}}],
				[{name:'s8'}, {name:'s9',value:{colorValue:'gold'}}],
				[{name:'s9'}, {name:'s10',value:{colorValue:'gold'}}],
				[{name:'s10'}, {name:'s11',value:{colorValue:'gold'}}],
		]
		},
	  markPoint:{
			symbol:'emptyCircle',
			symbolSize:function(v){
				return v/5
			},
			effect:{
			    show:true,
                type:'scale',
                period:10,
                color:'gold',				
			},
			itemStyle:{
				normal:{
					label:{
						show:false,
					},
				},
				emphasis:{
					label:{
						show:false,
					},
				},
			},
			data:[
			   {name:'s1',value:50,
			       tooltip:{
					   formatter:'小乙<br/>时间:8:30am<br/>出发地:东兴小区'
				   },
			   },
			   {name:'s5',value:50,
			       tooltip:{
					   formatter:'小丙<br/>时间:8:10am<br/>出发地:冼村'
				   },
			   },
			   {name:'s10',value:50,
			       //tooltip:{
				   //   formatter:'出发地上海南站<br/>经度:121.326966<br/>纬度:31.200723'  
				   //},
			   },
			   {name:'s11',value:100,
			       tooltip:{
					   formatter:'时间:10:00am<br/>目的地:上海南站<br/>出发地点<br/>开始一天的工作'
				   },
			   },
			],
		},
      geoCoord:{
                 's1':[121.326966,31.200723],
                 's2':[121.328966,31.220723],
                 's3':[121.336966,31.240723],
                 's4':[121.451855,31.251429],
                 's5':[121.461855,31.256429],
                 's6':[121.460855,31.257429],
                 's7':[121.458855,31.257729],
                 's8':[121.456855,31.257829],
                 's9':[121.454855,31.257929],
                 's10':[121.446394,31.259887],
                 's11':[121.432394,31.259987],
    }
},
	
    ]
};


var myChart = BMapExt.initECharts(container);
window.onresize = myChart.onresize;
BMapExt.setOption(option);
                }
                );
                })();

