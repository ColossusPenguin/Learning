// Find the Cost per Tile to cover WxH Floor

import scala.math.BigDecimal; import scala.io.StdIn; object
floorTileCost extends App { var cost = 0.00 var price = 0.00 var
height = 0.00 var width = 0.00 println("Enter the cost per square area
of tile: ") price = scala.io.StdIn.readLine().toDouble println("Enter
the width of the floor") width = scala.io.StdIn.readLine().toDouble
println("Enter the height of the floor") height =
scala.io.StdIn.readLine().toDouble cost = height*width*price var
trueCost = BigDecimal(cost).setScale(2) println("The cost of covering
a "+width+" by "+height+" floor is $"+trueCost) }
